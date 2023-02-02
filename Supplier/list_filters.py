from django.contrib.admin import SimpleListFilter
from .models import Supplier
from .supportmodels import Fields
from django.utils.translation import gettext as _

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

#Tính năng Filter: chưa thấy bổ sung thêm Cost Range (<10tr, 10-30tr, 30tr-50tr, 50-70tr, 70-100tr, >100tr)
class CostRangeFilter(SimpleListFilter):
    title = 'Cost Range' # or use _('country') for translated title
    parameter_name = 'cost_range'

    def lookups(self, request, model_admin):
        return (
          ('1', _('< 10tr')),
          ('2', _('10-30tr')),
          ('3', _('30tr-50tr')),
          ('4', _('50-70tr')),
          ('5', _('70-100tr')),
          ('6', _('>100tr')),
       )

    def queryset(self, request, queryset):
        # to decide how to filter the queryset.
        # return queryset.filter(fields__contains=self.value())
        p10 = 10000000
        p30 = 30000000
        p50 = 50000000
        p70 = 70000000
        p100 = 100000000
        if self.value() == '1':
            return queryset.filter(original_cost_picture__lte=p10) \
                | queryset.filter(original_cost_video__lte=p10) \
                | queryset.filter(original_cost_event__lte=p10) \
                | queryset.filter(original_cost_tvc__lte=p10)

        if self.value() == '2':
            return queryset.filter(original_cost_picture__gte=p10, original_cost_picture__lte=p30) \
                | queryset.filter(original_cost_video__gte=p10, original_cost_video__lte=p30) \
                | queryset.filter(original_cost_event__gte=p10, original_cost_event__lte=p30) \
                | queryset.filter(original_cost_tvc__gte=p10, original_cost_tvc__lte=p30) \
                
        if self.value() == '3':
            return queryset.filter(original_cost_picture__gte=p30, original_cost_picture__lte=p50) \
                | queryset.filter(original_cost_video__gte=p30, original_cost_video__lte=p50) \
                | queryset.filter(original_cost_event__gte=p30, original_cost_event__lte=p50) \
                | queryset.filter(original_cost_tvc__gte=p30, original_cost_tvc__lte=p50)
        if self.value() == '4':
            return queryset.filter(original_cost_picture__gte=p50, original_cost_picture__lte=p70) \
                | queryset.filter(original_cost_video__gte=p50, original_cost_video__lte=p70) \
                | queryset.filter(original_cost_event__gte=p50, original_cost_event__lte=p70) \
                | queryset.filter(original_cost_tvc__gte=p50, original_cost_tvc__lte=p70)
        if self.value() == '5':
            return queryset.filter(original_cost_picture__gte=p70, original_cost_picture__lte=p100) \
                | queryset.filter(original_cost_video__gte=p70, original_cost_video__lte=p100) \
                | queryset.filter(original_cost_event__gte=p70, original_cost_event__lte=p100) \
                | queryset.filter(original_cost_tvc__gte=p70, original_cost_tvc__lte=p100)
        if self.value() == '6':
            return queryset.filter(original_cost_picture__gte=p100) \
                | queryset.filter(original_cost_video__gte=p100)  \
                | queryset.filter(original_cost_event__gte=p100) \
                | queryset.filter(original_cost_tvc__gte=p100) 
