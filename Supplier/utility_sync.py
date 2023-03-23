from Supplier.models import Supplier
from siteconfig.models import BackgroundLog, SyncConfig
import datetime
from Supplier.utility import *
from Supplier.utility_numbers import *
from django.utils import timezone

class SyncUtility:
    def should_sync(self):
        should_sync = True
        x_date = datetime.date.today()
        no = x_date.weekday()
        self.saveLog(None, 'should_sync today is %s' % no, True)

        for config in SyncConfig.objects.all():
            if config.name == 'Sync follower' :
                should_sync = (no == 0 and config.mon) or \
                            (no == 1 and config.tue) or \
                            (no == 2 and config.wed) or \
                            (no == 3 and config.thu) or \
                            (no == 4 and config.fri) or \
                            (no == 5 and config.sat) or \
                            (no == 6 and config.sun)
                break
        return should_sync

    def sync_follower(self, start_page = 0):
        logObj = self.saveLog(None, 'sync_follower START,', True)
        failDatas = []
        should_sync = self.should_sync()
        if should_sync == False:
            logObj = self.saveLog(logObj, 'Stop by config,', True)
            return

        count = Supplier.objects.count()
        pages = int(count/500) + 1
        logObj = self.saveLog(logObj, 'split to %s pages'%pages, True)
        for p in range(pages):
            if p >= start_page:
                self.sync_page(p)
        logObj = self.saveLog(logObj, 'sync_follower END, ', True)
        if len(failDatas) > 0:
            self.sync_follower_recheck(failDatas)

    def sync_page(self, page, pSize = 500):
        logObj = self.saveLog(None, 'sync_page (%s, %s) START,'%(page, pSize), True)
        maxId = (page + 1) * pSize
        minId = page * pSize
        allSuppliers = Supplier.objects.filter(id__lte=maxId).filter(id__gte=minId).order_by('id')
        self.sync_suppliers(allSuppliers)
        temp_log = 'sync_page (%s, %s) End,'%(page, pSize)
        logObj = self.saveLog(logObj, temp_log, True)

    def sync_suppliers(self, suppliers):
        failDatas = []
        logObj = None
        logSuccess = None
        logFail = None
        driver = None
        logObj = self.saveLog(None, 'sync_suppliers START,', True)
        try:
            driver = prepare_driver(True)
        except:
            logObj = self.saveLog(logObj, 'Init driver fail,', True)
            return

        for obj in suppliers:
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
                    failDatas.append(obj)
                    temp_log = (obj.name + '(%s),' % (obj.id) )
                    logFail = self.saveLog(logFail, temp_log, False)
        if driver:
            logObj = self.saveLog(logObj, 'Close Driver, ', True)
            try:
                close_driver(driver)
                driver = None
            except:
                pass

        if len(failDatas) > 0:
            pass
            #self.sync_follower_recheck(failDatas)
        logObj = self.saveLog(logObj, 'sync_suppliers END', True)

    def sync_follower_recheck(self, datas):
        logObj = self.saveLog(None, 'Recheck (%s) start,'%len(datas), True)
        driver = None
        logSuccess = None
        logFail = None
        try:
            driver = prepare_driver(True)
        except:
            logObj = self.saveLog(logObj, 'Init driver fail,', True)
            return
        allSuppliers = datas
        for obj in allSuppliers:
            if support_sync(obj.channel):
                logObj = self.saveLog(logObj, '%s, '% obj.id, True)
                result = read_followers(driver, obj)
                if result > 0:
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
        logInstance = logObj
        if logInstance == None:
            logInstance = BackgroundLog(log = textLog, isSuccess = isSuccess)
        else:
            logInstance.log = logInstance.log + textLog
            logInstance.time = timezone.now()
        
        logInstance.save()
    
        if len(logInstance.log) > 10000:
            textLog = ''
            logInstance = BackgroundLog(log = textLog, isSuccess = isSuccess)
    
        return logInstance
