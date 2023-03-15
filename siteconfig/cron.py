from Supplier.models import Supplier
from .models import BackgroundLog, SyncConfig
from Supplier.utility import *
from Supplier.utility_numbers import *
import datetime

def sync_follower():
    log = 'Thread Start,'
    logObj = BackgroundLog(log = log)
    logObj.log = log
    logObj.save()
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
        log += '\n Stop by config, '
        logObj.log = log
        logObj.save()
        return

    log += '\n Start Sync config,'
    logObj.log = log
    logObj.save()
    successText = ''
    failText = ''
    logSuccess = BackgroundLog(log = successText)
    logFail = BackgroundLog(log = failText, isSuccess = False)
    
    driver = prepare_driver(True)
    for obj in Supplier.objects.all():
        if support_sync(obj.channel):
            result = read_followers(driver, obj)
            if result > 0:
                old_follower = obj.follower
                new_follwer = convert_to_string_number(result)
                obj.follower = new_follwer
                if old_follower != new_follwer:
                    try:
                        obj.save()
                        successText += (obj.name + '(%s -> %s),\n' % (str(old_follower or ''), str(obj.follower or '')))
                        logSuccess.log = successText
                        logSuccess.save()
                        if len(successText) > 1000:
                            successText = ''
                            logSuccess = BackgroundLog(log = successText)

                    except Exception as e:
                        failText += (obj.name + '(Save fail %s -> %s),\n' % (str(old_follower or ''), str(obj.follower or '')))
                        logFail.log = failText
                        logFail.save()
                        if len(failText) > 1000:
                            failText = ''
                            logFail = BackgroundLog(log = failText, isSuccess = False)
                else:
                    successText += (obj.name + '(-),\n')
                    logSuccess.log = successText
                    logSuccess.save()

            else:
                failText += (obj.name + '(%s),\n' % (obj.channel) )
                logFail.log = failText
                logFail.save()
                if len(failText) > 1000:
                    failText = ''
                    logFail = BackgroundLog(log = failText, isSuccess = False)
    log += '\n Finish loop all database '
    logObj.log = log
    logObj.save()
    
    if driver:
        log += '\n Close Driver, '
        logObj.log = log
        logObj.save()
        try:
            close_driver(driver)
            driver = None
        except:
            pass
    
    log += '\n Thread End'
    logObj.log = log
    logObj.save()