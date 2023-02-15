from Supplier.models import Supplier
from .models import BackgroundLog, SyncConfig
from .utility import *
import datetime

def sync_follower():
    print('sync_follower Start')
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
        print('sync_follower Start by config')
        successText = ''
        failText = ''
        logSuccess = BackgroundLog(log = successText)
        logFail = BackgroundLog(log = failText, isSuccess = False)

        for obj in Supplier.objects.all():
            result = read_followers(obj.link, obj.channel)
            if result > 0:
                old_follower = obj.follower
                obj.follower = convert_to_string_number(result)
                try:
                    obj.save()
                    successText += (obj.name + '(Updated from %s -> %s)\n' % (old_follower, obj.follower))
                    logSuccess.log = successText
                    logSuccess.save()
                except Exception as e:
                    failText += (obj.name + '(Save fail from %s -> %s)\n' % (old_follower, obj.follower))
                    logFail.save()
            else:
                failText += (obj.name + '(fetch fail, try update manual)\n')
                logFail.save()
    else:
        print('sync_follower Stop by config')

    print('sync_follower End')

    