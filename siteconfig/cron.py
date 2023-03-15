from Supplier.models import Supplier
from .models import BackgroundLog, SyncConfig
from Supplier.utility import *
from Supplier.utility_numbers import *
import datetime

def sync_follower():
    logObj= saveLog(None, 'Thread Start,', True)

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
        logObj = saveLog(logObj, '\n Stop by config, ', True)
        return

    logObj = saveLog(logObj, '\n Start Sync config,', True)
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
                        logSuccess = saveLog(logSuccess, temp_log, True)
                    except:
                        temp_log = obj.name + '(Save fail %s -> %s),\n' % (str(old_follower or ''), str(obj.follower or ''))
                        logFail = saveLog(logFail, temp_log, False)
                else:
                    temp_log = (obj.name + '(-),\n')
                    logSuccess = saveLog(logSuccess, temp_log, True)

            else:
                temp_log = (obj.name + '(%s),\n' % (obj.channel) )
                logFail = saveLog(logFail, temp_log, False)
    temp_log = '\n Finish loop all database '
    logObj = saveLog(logObj, temp_log, True)
    
    if driver:
        logObj = saveLog(logObj, '\n Close Driver, ', True)
        try:
            close_driver(driver)
            driver = None
        except:
            pass
    temp_log = '\n Thread End'
    logObj = saveLog(logObj, temp_log, True)

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