from django.db import models

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

class BackgroundLog(models.Model):
    log = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    isSuccess = models.BooleanField(default = True, null=True)
