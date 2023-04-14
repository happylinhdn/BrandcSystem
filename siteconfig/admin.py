from django.contrib import admin
from .models import BackgroundLog, SyncConfig, BackgroundLogDevOnly

# Register your models here.
@admin.register(SyncConfig)
class SyncConfigAdmin(admin.ModelAdmin):
    readonly_fields=('name', )
    list_display = ['id', 'name', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    fieldsets = (
    ('Info', {
        'fields': ('name', )
    }),
    ('Weekday', {
        'fields': (
            ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'), )
    }),
)

@admin.register(BackgroundLog)
class BackgroundLogAdmin(admin.ModelAdmin):
    readonly_fields=('time', 'log', 'isSuccess')
    list_display = ['id', 'isSuccess','log','time']
    search_fields = ['log']
    list_filter = ['isSuccess']