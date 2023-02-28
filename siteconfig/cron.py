from Supplier.models import Supplier
from .models import BackgroundLog, SyncConfig
from Supplier.utility import *
import datetime

def sync_follower():
    log = 'sync_follower Start'
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
    
    if should_sync:
        log += '\n sync_follower Start by config'
        successText = ''
        failText = ''
        logSuccess = BackgroundLog(log = successText)
        logFail = BackgroundLog(log = failText, isSuccess = False)

        for obj in Supplier.objects.all():
            result = read_followers(obj.link, obj.channel)
            if result > 0:
                old_follower = obj.follower
                new_follwer = convert_to_string_number(result)
                obj.follower = new_follwer
                if old_follower != new_follwer:
                    try:
                        obj.save()
                        successText += (obj.name + '-' + str(obj.id) + '(%s -> %s)\n' % (old_follower, obj.follower))
                        logSuccess.log = successText
                        logSuccess.save()
                        if len(successText) > 1000:
                            successText = ''
                            logSuccess = BackgroundLog(log = successText)

                    except Exception as e:
                        failText += (obj.name + '-' + str(obj.id) + '(Save fail from %s -> %s)\n' % (old_follower, obj.follower))
                        logFail.log = failText
                        logFail.save()
                        if len(failText) > 1000:
                            failText = ''
                            logFail = BackgroundLog(log = failText, isSuccess = False)
                else:
                    successText += (obj.name + '-' + str(obj.id) + '(Same)\n')
                    logSuccess.log = successText
                    logSuccess.save()

            else:
                failText += (obj.name + '-' + str(obj.id) + '\n')
                logFail.log = failText
                logFail.save()
                if len(failText) > 1000:
                    failText = ''
                    logFail = BackgroundLog(log = failText, isSuccess = False)
    else:
        log += '\n sync_follower Stop by config'

    log += '\n sync_follower End'
    logObj = BackgroundLog(log = log)
    logObj.log = log
    logObj.save()

    