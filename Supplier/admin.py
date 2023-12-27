# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import gettext as _
from .models import SupplierModel
from .list_filters import IndustryFilter, CostRangeFilter, YearRangeFilter, KPIRangeFilter
from .forms import SupplierForm
from .actions import ExportCsvMixin
from .resources import SupplierResource
from django.utils.html import format_html
from import_export.admin import ExportMixin, ExportActionMixin, ExportActionModelAdmin, ImportExportActionModelAdmin
from import_export.admin import ImportExportMixin, ImportMixin
import validators
from validators import ValidationFailure

def is_string_an_url(url_string: str) -> bool:
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        return False

    return result

from django.core.paginator import Paginator

class CustomPaginator(Paginator):
    """
    Paginator that does not count the rows in the table.
    """
    @property
    def count(self):
        try:
            return self.object_list.count()
        except (AttributeError, TypeError):
            return len(self.object_list)

# Register your models here.
@admin.register(SupplierModel)
class SupplierAdmin(ImportMixin, admin.ModelAdmin, ExportCsvMixin):
    list_select_related = True
    class Media:
        css = {
            'all': ('css/fancy.css',)
        }
    form = SupplierForm
    # paginator = CustomPaginator

    fieldsets = (
        ('ABOUT KOL', {
            'fields': ('name', ('link', 'channel','follower') , 'engagement_rate_percent', ('location', 'year_of_birth', 'gender'), 'industries')
        }),
        ('ABOUT SUPPLIER', {
            'fields': (
                ('original_cost_picture', 'original_cost_video', 'original_cost_event', 'original_cost_tvc', 'original_cost_livestream'), 
                ('kpi', 'note'), 
                ('supplier_name', 
                'booking_contact_name', 'booking_contact_phone', 'booking_contact_email'), 'profile', 'latest_update')
        }),
        ('ABOUT INTERNAL TEAM', {
            'fields': ('handle_by', ('group_chat_name', 'group_chat_channel'), 'lana_leader', 'modified_by')
        }),
    )

    list_display = ['id', 'name', 'channel_display', 'follower', 'kol_tier', 'engagement_rate_percent', 'engagement_rate_absolute_display', 
    'location', 'year_display', 'gender', 'industries', 'original_cost_picture_display', 'original_cost_video_display', 'original_cost_event_display', 'original_cost_tvc_display','original_cost_livestream_display',
    'kpi', 'note', 'supplier_name', 'booking_contact', 'profile_display', 'latest_update', 'handle_by', 'group_chat_name',
    'group_chat_channel', 'lana_leader' , 'modified_by'
    ]
    list_display_links  = ['name',]
    list_filter = [KPIRangeFilter, CostRangeFilter, 'kol_tier', 'handle_by', 'gender', 'channel', IndustryFilter, YearRangeFilter, 'location']
    search_fields = ['name', 'link']
    list_per_page = 25
    actions = ['export_as_xls', 'sync_follower']
    ordering = ['id']

    def original_cost_video_display(self, obj):
        return "{:,}".format(obj.original_cost_video or 0)
    
    def original_cost_picture_display(self, obj):
        return "{:,}".format(obj.original_cost_picture or 0)
    
    def original_cost_event_display(self, obj):
        return "{:,}".format(obj.original_cost_event or 0)
    def original_cost_tvc_display(self, obj):
        return "{:,}".format(obj.original_cost_tvc or 0)
    
    def original_cost_livestream_display(self, obj):
        return "{:,}".format(obj.original_cost_livestream or 0)
    

    def booking_contact(self, obj):
        return """Name:{0} - Phone: {1} - Email:{2}""".format(obj.booking_contact_name or '-', obj.booking_contact_phone or '-', obj.booking_contact_email or '-')
    
    def profile_display(self, obj):
        if obj.profile and is_string_an_url(obj.profile):
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