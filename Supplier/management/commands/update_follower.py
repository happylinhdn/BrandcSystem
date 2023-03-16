from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier
from siteconfig.models import BackgroundLog, SyncConfig
from Supplier.utility import *
from Supplier.utility_numbers import *
import datetime

class Command(BaseCommand):
    help = 'Update follower'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call update_follower command success, checking arg'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier "%s"' % count))
        self.sync_follower()
    
    def saveLog(self, logObj, textLog, isSuccess = True):
        if isSuccess:
            self.stdout.write(self.style.SUCCESS(textLog))
        else:
            self.stdout.write(self.style.WARNING(textLog))
        logInstance = logObj
        if logInstance == None:
            logInstance = BackgroundLog(log = textLog, isSuccess = isSuccess)
        else:
            logInstance.isSuccess = isSuccess
            logInstance.log = logInstance.log + textLog
        
        logInstance.save()
    
        if len(logInstance.log) > 5000:
            textLog = ''
            logInstance = BackgroundLog(log = textLog, isSuccess = isSuccess)
    
        return logInstance

    def sync_follower(self):
        logObj = self.saveLog(None, 'Thread Start by command,', True)
        failDatas = []

        should_sync = True
        
        x_date = datetime.date.today()
        no = x_date.weekday()

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
        driver = None
        if should_sync == False:
            logObj = self.saveLog(logObj, 'Stop by config,', True)
            return

        logObj = self.saveLog(logObj, 'Start Sync config,', True)
        logSuccess = BackgroundLog(log = '')
        logFail = BackgroundLog(log = '', isSuccess = False)
        
        # try:
        #     driver = prepare_driver(True)
        # except:
        #     logObj = self.saveLog(None, 'Init driver fail,', True)
        #     return
        # allSuppliers = Supplier.objects.order_by('id')
        count = Supplier.objects.count()
        pages = int(count/500) + 1
        print('will split to %s browser'%pages)
        for p in range(pages):
            self.sync_page(p)

        # for obj in allSuppliers:
        #     if support_sync(obj.channel):
        #         logObj = self.saveLog(logObj, '%s, '% obj.id, True)
        #         result = read_followers(driver, obj)
        #         if result > 0:
        #             old_follower = obj.follower
        #             new_follwer = convert_to_string_number(result)
        #             obj.follower = new_follwer

        #             if old_follower != new_follwer:
        #                 try:
        #                     obj.save()
        #                     temp_log = (obj.name + '(%s -> %s),' % (str(old_follower or ''), str(obj.follower or '')))
        #                     logSuccess = self.saveLog(logSuccess, temp_log, True)
        #                 except:
        #                     temp_log = obj.name + '(Save fail %s -> %s),' % (str(old_follower or ''), str(obj.follower or ''))
        #                     logFail = self.saveLog(logFail, temp_log, False)
        #                     failDatas.append(obj)
        #             else:
        #                 temp_log = (obj.name + '(-),')
        #                 logSuccess = self.saveLog(logSuccess, temp_log, True)

        #         else:
        #             temp_log = (obj.name + '(%s),' % (obj.id) )
        #             logFail = self.saveLog(logFail, temp_log, False)
        #             failDatas.append(obj)
        # temp_log = 'Finish loop database, '
        # logObj = self.saveLog(logObj, temp_log, True)
        
        # if driver:
        #     logObj = self.saveLog(logObj, 'Close Driver, ', True)
        #     try:
        #         close_driver(driver)
        #         driver = None
        #     except:
        #         pass
        temp_log = 'Thread End, '
        logObj = self.saveLog(logObj, temp_log, True)
        if len(failDatas) > 0:
            self.sync_follower_recheck(failDatas)

    def sync_page(self, page, pSize = 500):
        logObj = self.saveLog(None, 'sync_page (%s, %s) start,'%(page, pSize), True)
        driver = None
        logSuccess = None
        logFail = None
        try:
            driver = prepare_driver(True)
        except:
            logObj = self.saveLog(None, 'Init driver fail,', True)
            return
        maxId = (page + 1) * pSize
        minId = page * pSize
        allSuppliers = Supplier.objects.filter(id__lte=maxId).filter(id__gte=minId).order_by('id')
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
                            temp_log = (obj.name + '(%s -> %s),' % (str(old_follower or ''), str(obj.follower or '')))
                            logSuccess = self.saveLog(logSuccess, temp_log, True)
                        except:
                            temp_log = obj.name + '(Save fail %s -> %s),' % (str(old_follower or ''), str(obj.follower or ''))
                            logFail = self.saveLog(logFail, temp_log, False)
                    else:
                        temp_log = (obj.name + '(-),')
                        logSuccess = self.saveLog(logSuccess, temp_log, True)

                else:
                    temp_log = (obj.name + '(%s),' % (obj.id) )
                    logFail = self.saveLog(logFail, temp_log, False)
        temp_log = 'Finish loop, '
        logObj = self.saveLog(logObj, temp_log, True)
        
        if driver:
            logObj = self.saveLog(logObj, 'Close Driver, ', True)
            try:
                close_driver(driver)
                driver = None
            except:
                pass
        temp_log = 'sync_page (%s, %s) End,'%(page, pSize)
        logObj = self.saveLog(logObj, temp_log, True)

    def sync_follower_recheck(self, datas):
        logObj = self.saveLog(None, 'Recheck (%s) start,'%len(datas), True)
        driver = None
        logSuccess = None
        logFail = None
        try:
            driver = prepare_driver(True)
        except:
            logObj = self.saveLog(None, 'Init driver fail,', True)
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
                            temp_log = (obj.name + '(%s -> %s),' % (str(old_follower or ''), str(obj.follower or '')))
                            logSuccess = self.saveLog(logSuccess, temp_log, True)
                        except:
                            temp_log = obj.name + '(Save fail %s -> %s),' % (str(old_follower or ''), str(obj.follower or ''))
                            logFail = self.saveLog(logFail, temp_log, False)
                    else:
                        temp_log = (obj.name + '(-),')
                        logSuccess = self.saveLog(logSuccess, temp_log, True)

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






