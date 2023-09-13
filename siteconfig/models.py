from django.db import models
from django.utils.translation import gettext as _
from Supplier.supportmodels import SupplierChannel
import datetime

class SyncPlan(models.TextChoices):
    Weekly = 'Weekly', _('Weekly')
    BiWeekly = 'BiWeekly', _('BiWeekly')
    ThreeWeekly='ThreeWeekly', _('ThreeWeekly')
    FourWeekly='FourWeekly', _('FourWeekly')

# Create your models here.
class SyncConfig(models.Model):
    name = models.CharField(max_length=20)
    mon = models.BooleanField(default = True)
    tue = models.BooleanField(default = True)
    wed = models.BooleanField(default = True)
    thu = models.BooleanField(default = True)
    fri = models.BooleanField(default = True)
    sat = models.BooleanField(default = True)
    sun = models.BooleanField(default = True)
    plan = models.CharField(verbose_name='Plan', max_length=20, choices=SyncPlan.choices, null=True, default=SyncPlan.BiWeekly)
    last_date_sync = models.CharField(max_length=10, default = "2023-06-01") #"2023-07-17"
    handle_channel_synced = models.CharField(max_length=20, choices=SupplierChannel.choices, default = "Others")
    
    def __str__(self):
        return self.name
    
    def prepare_channel(self):
        supports = (
            SupplierChannel.FB_GROUP, SupplierChannel.FB_FANPAGE, SupplierChannel.FB_PERSONAL,
            SupplierChannel.TIKTOK_COMMUNITY, SupplierChannel.TIKTOK_PERSONAL, 
            SupplierChannel.YOUTUBE_COMMUNITY, SupplierChannel.YOUTUBE_PERSONAL,
            SupplierChannel.INSTAGRAM
        )
        index_current = -1
        try:
            index_current = supports.index(self.handle_channel_synced)
        except:
            index_current = -1
        next_index = index_current + 1
        if next_index > len(supports):
            next_index = 0
        
        self.handle_channel_synced = supports[next_index]
        today_date = datetime.date.today()
        self.last_date_sync = today_date.strftime("%Y-%m-%d")



class BackgroundLog(models.Model):
    log = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    isSuccess = models.BooleanField(default = True, null=True)

class BackgroundLogDevOnly(models.Model):
    log = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    isSuccess = models.BooleanField(default = True, null=True)

class FailLinkCacheModel(models.Model):
    time = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=300, null=True)