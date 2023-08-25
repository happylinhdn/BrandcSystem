from Supplier.models import SupplierModel
from Supplier.supportmodels import SupplierChannel
from siteconfig.models import BackgroundLog, SyncConfig, BackgroundLogDevOnly, SyncPlan
import datetime
from Supplier.utility import *
from Supplier.utility_numbers import *
from django.utils import timezone
from datetime import timedelta
import gc  
# from datetime import datetime


class SyncUtility:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of SyncUtility.")
        return super().__new__(cls)

    def __init__(self, forDev):
        print("2. Initialize the new instance of SyncUtility.")
        self.forDev = forDev

    def sync_channels(self):
        gc.collect()
        logObj = self.saveLog(None, 'START sync thread, ', True)
        should_sync = self.should_sync()
        print("3. Check should_sync = ", should_sync)
        if should_sync == False:
            logObj = self.saveLog(logObj, 'Stop sync thread by config, ', True)
        else:
            self.store_last_sync()
            for channel in SupplierChannel.choices:
                if support_sync(channel[0]):
                    self.sync_channel(channel[0])
                else:
                    logObj = self.saveLog(logObj, 'Skip sync this channel cause not support now, %s ' % channel[0], True)
            logObj = self.saveLog(logObj, 'Finish sync thread, ', True)
        # clean old log
        self.cleanOldLogs()

    def sync_channel(self, channel):
        suppliers = SupplierModel.objects.filter(channel=channel).order_by('id')
        count = suppliers.count()
        shouldSetupFb = suppliers.filter(channel=SupplierChannel.FB_PERSONAL).count() > 0 \
            or suppliers.filter(channel=SupplierChannel.FB_FANPAGE).count() > 0 \
                or suppliers.filter(channel=SupplierChannel.FB_GROUP).count() > 0
        shouldSetupInstagram = suppliers.filter(channel=SupplierChannel.INSTAGRAM).count() > 0
        self.saveLog(None, 'sync_channel %s with %s item START '%(channel, count), True)
        if count > 0:
            self.sync_suppliers(suppliers, shouldSetupFb, shouldSetupInstagram)
        self.saveLog(None, 'sync_channel %s END'%channel, True)

    def should_sync(self):
        is_correct_weekday = True
        today_date = datetime.date.today()
        no = today_date.weekday()
        #self.saveLog(None, 'should_sync today is %s' % no, True)
        last_date_sync = datetime.datetime.strptime("2023-06-01", "%Y-%m-%d") 
        next_date_sync = datetime.datetime.strptime("2023-06-15", "%Y-%m-%d") 
        plan = SyncPlan.BiWeekly


        for config in SyncConfig.objects.all():
            if config.name == 'Sync follower' :
                last_date_sync = datetime.datetime.strptime(config.last_date_sync, "%Y-%m-%d")  
                plan = config.plan
                is_correct_weekday = (no == 0 and config.mon) or \
                            (no == 1 and config.tue) or \
                            (no == 2 and config.wed) or \
                            (no == 3 and config.thu) or \
                            (no == 4 and config.fri) or \
                            (no == 5 and config.sat) or \
                            (no == 6 and config.sun)
                
                break
        if is_correct_weekday != True:
            return is_correct_weekday
        
        if plan == SyncPlan.Weekly:
            next_date_sync = last_date_sync + timedelta(weeks=1)
        elif plan == SyncPlan.BiWeekly:
            next_date_sync = last_date_sync + timedelta(weeks=2)
        elif plan == SyncPlan.ThreeWeekly:
            next_date_sync = last_date_sync + timedelta(weeks=3)
        else:
            next_date_sync = last_date_sync + timedelta(weeks=4)
        
        if next_date_sync.date() > today_date:
            return False
        else:
            return True

    def store_last_sync(self):
        today_date = datetime.date.today()
        for config in SyncConfig.objects.all():
            if config.name == 'Sync follower' :
                config.last_date_sync = today_date.strftime("%Y-%m-%d")
                config.save()
                break          

    def sync_follower(self, start_page = 0):
        logObj = self.saveLog(None, 'START, ', True)
        should_sync = self.should_sync()
        if should_sync == False:
            logObj = self.saveLog(logObj, 'Stop by config, ', True)
            return

        self.store_last_sync()

        count = SupplierModel.objects.count()
        pages = int(count/500) + 1
        logObj = self.saveLog(logObj, 'split to %s pages '%pages, True)
        for p in range(pages):
            if p >= start_page:
                self.sync_page(p)
        logObj = self.saveLog(logObj, 'END, ', True)

    def sync_page(self, page, pSize = 500):
        logObj = self.saveLog(None, 'Page (%s, %s) START, '%(page, pSize), True)
        maxId = (page + 1) * pSize
        minId = page * pSize
        allSuppliers = SupplierModel.objects.filter(id__lte=maxId).filter(id__gte=minId).order_by('id')
        shouldSetupFb = allSuppliers.filter(channel=SupplierChannel.FB_PERSONAL).count() > 0 or \
            allSuppliers.filter(channel=SupplierChannel.FB_FANPAGE).count() > 0 or \
                allSuppliers.filter(channel=SupplierChannel.FB_GROUP).count() > 0
        shouldSetupInstagram = allSuppliers.filter(channel=SupplierChannel.INSTAGRAM).count() > 0

        self.sync_suppliers(allSuppliers, shouldSetupFb, shouldSetupInstagram)
        temp_log = 'Page (%s, %s) End,'%(page, pSize)
        logObj = self.saveLog(logObj, temp_log, True)

    def sync_suppliers(self, suppliers, shouldSetupFb = True, shouldSetupInstagram = True):
        failDatas = []
        logObj = None
        logFail = None
        driver = None
        logObj = self.saveLog(None, 'sync_suppliers START ', True)
        gap_memory = 0
        init_driver_counter = 0
        # try:
        #     driver = prepare_driver(shouldSetupFb, shouldSetupInstagram)
        # except:
        #     logFail = self.saveLog(logFail, 'Init driver fail, ', False)
        #     return

        for obj in suppliers:
            if support_sync(obj.channel):
                if gap_memory == 0 or driver is None:
                    try:
                        if driver:
                            try:
                                logObj = self.saveLog(logObj, 'Close Driver %s, ' % str(init_driver_counter), True)
                                close_driver(driver)
                                driver = None
                            except:
                                pass
                        gc.collect()
                        logObj = self.saveLog(logObj, 'Init driver %s, '% str(init_driver_counter), True)
                        init_driver_counter = init_driver_counter + 1
                        driver = prepare_driver(shouldSetupFb, shouldSetupInstagram)
                    except:
                        logFail = self.saveLog(logFail, 'Init driver fail, ', False)
                        return
                
                gap_memory = gap_memory + 1
                if gap_memory > 100:
                    gap_memory = 0

                logObj = self.saveLog(logObj, '%s, '% obj.id, True)
                result = read_followers(driver, obj)
                if result >= 0:
                    old_follower = obj.follower
                    new_follwer = convert_to_string_number(result)
                    obj.follower = new_follwer

                    if old_follower != new_follwer:
                        try:
                            obj.save()
                        except:
                            temp_log = obj.name + '(Save fail %s -> %s),' % (str(old_follower or ''), str(obj.follower or ''))
                            logFail = self.saveLog(logFail, temp_log, False)
                else:
                    failDatas.append(obj)
                    temp_log = (obj.name + '(%s),' % (obj.id) )
                    logFail = self.saveLog(logFail, temp_log, False)
        if driver:
            logObj = self.saveLog(logObj, 'Close Driver, ', True)
            try:
                close_driver(driver)
                driver = None
            except:
                logFail = self.saveLog(logFail, 'Close Driver Fail, ', False)
                pass

        if len(failDatas) > 0:
            logObj = self.saveLog(logObj, 'sync_suppliers END with %s fail items' % len(failDatas), True)
        else:
            logObj = self.saveLog(logObj, 'sync_suppliers END', True)

    def sync_follower_recheck(self, datas):
        logObj = self.saveLog(None, 'Recheck (%s) start,'%len(datas), True)
        driver = None
        logFail = None
        try:
            driver = prepare_driver(True, True)
        except:
            logObj = self.saveLog(logObj, 'Init driver fail,', True)
            return
        allSuppliers = datas
        for obj in allSuppliers:
            if support_sync(obj.channel):
                logObj = self.saveLog(logObj, '%s, '% obj.id, True)
                result = read_followers(driver, obj)
                if result >= 0:
                    old_follower = obj.follower
                    new_follwer = convert_to_string_number(result)
                    obj.follower = new_follwer

                    if old_follower != new_follwer:
                        try:
                            obj.save()
                            #temp_log = (obj.name + '(%s -> %s),' % (str(old_follower or ''), str(obj.follower or '')))
                            #logSuccess = self.saveLog(logSuccess, temp_log, True)
                        except:
                            temp_log = obj.name + '(Save fail %s -> %s),' % (str(old_follower or ''), str(obj.follower or ''))
                            logFail = self.saveLog(logFail, temp_log, False)
                    else:
                        pass
                        #temp_log = (obj.name + '(-),')
                        #logSuccess = self.saveLog(logSuccess, temp_log, True)

                else:
                    temp_log = (obj.name + '(%s),' % (obj.id) )
                    logFail = self.saveLog(logFail, temp_log, False)
        temp_log = 'Recheck finish loop, '
        logObj = self.saveLog(logObj, temp_log, True)
        
        if driver:
            logObj = self.saveLog(logObj, 'Recheck Close Driver, ', True)
            try:
                close_driver(driver)
                driver = None
            except:
                pass
        temp_log = 'Recheck End, '
        logObj = self.saveLog(logObj, temp_log, True)

    def saveLog(self, logObj, textLog, isSuccess = True):
        print('write log:', textLog)
        try:
            logInstance = logObj
            if logInstance == None:
                logInstance = self.getLog(textLog, isSuccess)
            else:
                logInstance.log = logInstance.log + textLog
                logInstance.time = timezone.now()
            
            logInstance.save()
        
            if len(logInstance.log) > 5000:
                logInstance = self.getLog('', isSuccess)
        
            return logInstance
        except:
            print('Error when save log', textLog)
            return None
        
    def getLog(self, textLog, isSuccess):
        if self.forDev:
            return BackgroundLogDevOnly(log = textLog, isSuccess = isSuccess)
        else:
            return BackgroundLog(log = textLog, isSuccess = isSuccess)
    
    def cleanOldLogs(self):
        aPastWeek = timezone.now() - timedelta(days=7)
        oldDB = BackgroundLog.objects.filter(time__lte=aPastWeek)
        count = oldDB.count()
        if count > 0:
            oldDB.delete()