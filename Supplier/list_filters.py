from django.contrib.admin import SimpleListFilter
from .models import Supplier
from .supportmodels import Fields

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