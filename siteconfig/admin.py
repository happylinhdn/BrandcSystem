from django.contrib import admin
from .models import BackgroundLog, SyncConfig, FailLinkCacheModel

# Register your models here.
@admin.register(SyncConfig)
class SyncConfigAdmin(admin.ModelAdmin):
    readonly_fields=('name', )
    list_display = ['id', 'name', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'plan', 'last_date_sync', 'handle_channel_synced']
    fieldsets = (
    ('Info', {
        'fields': ('name', )
    }),
    ('Plan', {
        'fields': ('plan', )
    }),
    ('Weekday', {
        'fields': (
            ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'), )
    }),
    ('Log', {
        'fields': ('last_date_sync', 'handle_channel_synced')
    }),
)

@admin.register(BackgroundLog)
class BackgroundLogAdmin(admin.ModelAdmin):
    readonly_fields=('time', 'log', 'isSuccess')
    list_display = ['id', 'isSuccess','log','time']
    search_fields = ['log']
    list_filter = ['isSuccess']

@admin.register(FailLinkCacheModel)
class FailLinkCacheAdmin(admin.ModelAdmin):
    readonly_fields=('time','name', 'link')
    list_display = ['id', 'time', 'name', 'link']
    search_fields = ['name', 'link']