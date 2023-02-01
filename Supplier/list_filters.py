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
        if self.value() == '1':
            return queryset.filter(original_cost_picture__lte=10000) \
                | queryset.filter(original_cost_video__lte=10000) \
                | queryset.filter(original_cost_event__lte=10000) \
                | queryset.filter(original_cost_tvc__lte=10000)

        if self.value() == '2':
            return queryset.filter(original_cost_picture__gte=10000, original_cost_picture__lte=30000) \
                | queryset.filter(original_cost_video__gte=10000, original_cost_video__lte=30000) \
                | queryset.filter(original_cost_event__gte=10000, original_cost_event__lte=30000) \
                | queryset.filter(original_cost_tvc__gte=10000, original_cost_tvc__lte=30000) \
                
        if self.value() == '3':
            return queryset.filter(original_cost_picture__gte=30000, original_cost_picture__lte=50000) \
                | queryset.filter(original_cost_video__gte=30000, original_cost_video__lte=50000) \
                | queryset.filter(original_cost_event__gte=30000, original_cost_event__lte=50000) \
                | queryset.filter(original_cost_tvc__gte=30000, original_cost_tvc__lte=50000)
        if self.value() == '4':
            return queryset.filter(original_cost_picture__gte=50000, original_cost_picture__lte=70000) \
                | queryset.filter(original_cost_video__gte=50000, original_cost_video__lte=70000) \
                | queryset.filter(original_cost_event__gte=50000, original_cost_event__lte=70000) \
                | queryset.filter(original_cost_tvc__gte=50000, original_cost_tvc__lte=70000)
        if self.value() == '5':
            return queryset.filter(original_cost_picture__gte=70000, original_cost_picture__lte=100000) \
                | queryset.filter(original_cost_video__gte=70000, original_cost_video__lte=100000) \
                | queryset.filter(original_cost_event__gte=70000, original_cost_event__lte=100000) \
                | queryset.filter(original_cost_tvc__gte=70000, original_cost_tvc__lte=100000)
        if self.value() == '6':
            return queryset.filter(original_cost_picture__gte=100000) \
                | queryset.filter(original_cost_video__gte=100000)  \
                | queryset.filter(original_cost_event__gte=100000) \
                | queryset.filter(original_cost_tvc__gte=100000) 
