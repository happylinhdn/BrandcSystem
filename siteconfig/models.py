from django.db import models
from django.utils.translation import gettext as _

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
    
    def __str__(self):
        return self.name


class BackgroundLog(models.Model):
    log = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    isSuccess = models.BooleanField(default = True, null=True)

class BackgroundLogDevOnly(models.Model):
    log = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    isSuccess = models.BooleanField(default = True, null=True)
