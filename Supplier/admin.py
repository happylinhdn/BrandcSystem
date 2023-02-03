from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Supplier
from .list_filters import FieldsFilter, CostRangeFilter
from .forms import SupplierForm
from .actions import ExportCsvMixin
from .resources import SupplierResource
from django.utils.html import format_html
from import_export.admin import ExportMixin, ExportActionMixin, ExportActionModelAdmin, ImportExportActionModelAdmin
from import_export.admin import ImportExportMixin, ImportMixin


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(ImportMixin, admin.ModelAdmin, ExportCsvMixin):
    class Media:
        css = {
            'all': ('css/fancy.css',)
        }
    form = SupplierForm
    indexCnt = 0

    def index_counter(self, obj):
        count = Supplier.objects.all().count()
        if self.indexCnt < count:
            self.indexCnt += 1
        else:
            self.indexCnt = 1
        return self.indexCnt

    index_counter.short_description = '#'

    fieldsets = (
        ('ABOUT KOL', {
            'fields': ('name', ('link', 'channel','follower') , 'engagement_rate_percent', ('location', 'year_of_birth', 'gender'), 'fields')
        }),
        ('ABOUT SUPPLIER', {
            'fields': (
                ('original_cost_picture', 'original_cost_video', 'original_cost_event', 'original_cost_tvc'), 
                ('kpi', 'discount'), 
                ('supplier_name', 
                'booking_contact_name', 'booking_contact_phone', 'booking_contact_email'), 'profile', 'latest_update')
        }),
        ('ABOUT INTERNAL TEAM', {
            'fields': ('handle_by', ('group_chat_name', 'group_chat_channel'), 'lana_leader', 'modified_by')
        }),
    )

    list_display = ['index_counter', 'name', 'channel_display', 'follower', 'kol_tier', 'engagement_rate_percent', 'engagement_rate_absolute_display', 
    'location', 'year_display', 'gender', 'fields', 'original_cost_picture', 'original_cost_video', 'original_cost_event', 'original_cost_tvc',
    'kpi', 'discount', 'supplier_name', 'booking_contact', 'profile_display', 'latest_update', 'handle_by', 'group_chat_name',
    'group_chat_channel', 'lana_leader' , 'modified_by'
    ]
    list_display_links  = ['name',]
    list_filter = [CostRangeFilter, 'kol_tier', 'gender', 'year_of_birth', 'channel', FieldsFilter, 'location', ]
    search_fields = ['name', 'link']
    list_per_page = 25
    actions = ["export_as_xls"]

    
    def booking_contact(self, obj):
        return """Name:{0} - Phone: {1} - Email:{2}""".format(obj.booking_contact_name or '-', obj.booking_contact_phone or '-', obj.booking_contact_email or '-')
    
    def profile_display(self, obj):
        if obj.profile:
            return format_html("<a href='{url}'  target='_blank' >{name}</a>", url=obj.profile, name='Link')
        return "-"
    profile_display.short_description = 'PROFILE/QUOTATION'

    def year_display(self, obj):
        if obj.year_of_birth:
            return "{0}".format(obj.year_of_birth)
        return "-"
    year_display.short_description = 'Year'

    def channel_display(self, obj):
        return format_html("<a href='{url}'  target='_blank' >{name}</a>", url=obj.link, name=obj.channel)
    channel_display.short_description = 'Channel'

    def engagement_rate_absolute_display(self, obj):
        return obj.engagement_rate_absolute_display_calc() 
    engagement_rate_absolute_display.short_description = 'ER (Ab.)'

    resource_classes = [SupplierResource]

    def has_import_permission(self, request):
        has_perm = request.user.has_perm('Supplier.import_data_as_admin')
        return has_perm
