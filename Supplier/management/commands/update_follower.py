from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier
from siteconfig.models import BackgroundLog, SyncConfig
from Supplier.utility import *
from Supplier.utility_numbers import *
import datetime

def saveLog(logObj, textLog, isSuccess = True):
    if logObj == None:
        logObj = BackgroundLog(log = textLog)
    else:
        logObj.isSuccess = isSuccess
        logObj.log = logObj.log + textLog
    
    logObj.save()
    
    if len(textLog) > 1000:
        textLog = ''
        logObj = BackgroundLog(log = textLog, isSuccess = isSuccess)

    return logObj

class Command(BaseCommand):
    help = 'Update follower'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call update_follower command success, checking arg'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier "%s"' % count))
        self.sync_follower()
    
    def saveLog(self, logObj, textLog, isSuccess = True):
        self.stdout.write(self.style.SUCCESS(textLog))
        if logObj == None:
            logObj = BackgroundLog(log = textLog)
        else:
            logObj.isSuccess = isSuccess
            logObj.log = logObj.log + textLog
        
        logObj.save()
    
        if len(textLog) > 1000:
            textLog = ''
            logObj = BackgroundLog(log = textLog, isSuccess = isSuccess)
    
        return logObj

    def sync_follower(self):
        logObj= self.saveLog(None, 'Thread Start by command,', True)

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
            logObj = self.saveLog(logObj, '\n Stop by config, ', True)
            return

        logObj = self.saveLog(logObj, '\n Start Sync config,', True)
        logSuccess = BackgroundLog(log = '')
        logFail = BackgroundLog(log = '', isSuccess = False)
        
        driver = prepare_driver(True)
        allSuppliers = Supplier.objects.all()
        for obj in allSuppliers:
            if support_sync(obj.channel):
                result = read_followers(driver, obj)
                if result > 0:
                    old_follower = obj.follower
                    new_follwer = convert_to_string_number(result)
                    obj.follower = new_follwer

                    if old_follower != new_follwer:
                        try:
                            obj.save()
                            temp_log = (obj.name + '(%s -> %s),\n' % (str(old_follower or ''), str(obj.follower or '')))
                            logSuccess = self.saveLog(logSuccess, temp_log, True)
                        except:
                            temp_log = obj.name + '(Save fail %s -> %s),\n' % (str(old_follower or ''), str(obj.follower or ''))
                            logFail = self.saveLog(logFail, temp_log, False)
                    else:
                        temp_log = (obj.name + '(-),\n')
                        logSuccess = self.saveLog(logSuccess, temp_log, True)

                else:
                    temp_log = (obj.name + '(%s),\n' % (obj.channel) )
                    logFail = self.saveLog(logFail, temp_log, False)
        temp_log = '\n Finish loop all database '
        logObj = self.saveLog(logObj, temp_log, True)
        
        if driver:
            logObj = self.saveLog(logObj, '\n Close Driver, ', True)
            try:
                close_driver(driver)
                driver = None
            except:
                pass
        temp_log = '\n Thread End'
        logObj = self.saveLog(logObj, temp_log, True)






