from django.contrib import admin
from .models import BackgroundLog, SyncConfig

# Register your models here.
@admin.register(SyncConfig)
class BackgroundLogAdmin(admin.ModelAdmin):
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
    list_display = ['id', 'log', 'time', 'isSuccess']
    search_fields = ['log', 'time']
