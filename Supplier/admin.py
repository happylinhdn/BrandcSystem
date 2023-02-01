from django.contrib import admin
from .models import Supplier
from .supportmodels import Fields
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext as _

# Register your models here.
class FieldsFilter(SimpleListFilter):
    title = 'Fields' # or use _('country') for translated title
    parameter_name = 'field'

    def lookups(self, request, model_admin):
        all_choices = Fields.choices
        t_data = [c.fields for c in Supplier.objects.all()]
        result = []
        for choice in all_choices:
            for t in t_data:
                if choice[0] in t:
                    result.append(choice)
                    break
        return result

    def queryset(self, request, queryset):
        # to decide how to filter the queryset.
        # return queryset.filter(fields__contains=self.value())
        if self.value():
            return queryset.filter(fields__contains=self.value())

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'channel', 'follower', 'kol_tier', 'engagement_rate_percent', 'engagement_rate_absolute_display', 
    'location', 'year_of_birth', 'gender', 'fields', 'original_cost_picture', 'original_cost_video', 'original_cost_event', 'original_cost_tvc',
    'kpi', 'discount', 'supplier_name', 'booking_contact_display', 'profile_quotation', 'latest_update', 'handle_by', 'group_chat_name',
    'group_chat_channel', 'lana_leader' , 'modified_by'
    ]
    list_filter = ['kol_tier', 'gender', 'year_of_birth', 'channel', FieldsFilter, 'location', ]
    search_fields = ['name', 'link']

    def kol_tier_2(self, inst):
        return inst.kol_tier()

# Register your models here.
#admin.site.register(Supplier, SupplierAdmin)