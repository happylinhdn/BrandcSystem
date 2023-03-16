from django.contrib.admin import SimpleListFilter
from .models import Supplier
from .supportmodels import Fields, music_keys, entertainment_keys, sport_keys, financial_keys
from django.utils.translation import gettext as _

class FieldsFilter(SimpleListFilter):
    title = 'Fields' # or use _('country') for translated title
    parameter_name = 'field'

    def lookups(self, request, model_admin):
        MusicCategory = 'Music', _('Music')
        MusicKeys = music_keys()
        EntertainmentCategory = 'Entertainment', _('Entertainment')
        EntertainmentKeys = entertainment_keys()

        SportCategory = 'Sport', _('Sport')
        SportKeys = sport_keys()
        FinancialCategory = 'Financial', _('Financial')
        FinancialKeys = financial_keys()

        all_choices = Fields.choices
        others_fields = []
        all_music_fields = []
        all_entertainment_fields = []
        all_sport_fields = []
        all_financial_fields = []
        for c in all_choices:
            if c[0] in MusicKeys:
                all_music_fields.append(c)
            elif c[0] in EntertainmentKeys:
                all_entertainment_fields.append(c)
            elif c[0] in SportKeys:
                all_sport_fields.append(c)
            elif c[0] in FinancialKeys:
                all_financial_fields.append(c)
            else:
                others_fields.append(c)
            
        t_data = [c.fields for c in Supplier.objects.all()]
        result = []

        result.append(MusicCategory)
        for c in all_music_fields:
            result.append(c)

        result.append(EntertainmentCategory)
        for c in all_entertainment_fields:
            result.append(c)
        
        result.append(SportCategory)
        for c in all_sport_fields:
            result.append(c)

        result.append(FinancialCategory)
        for c in all_financial_fields:
            result.append(c)

        for choice in others_fields:
            for t in t_data:
                if choice[0] in t:
                    result.append(choice)
                    break
        return result

    def queryset(self, request, queryset):
        # to decide how to filter the queryset.
        # return queryset.filter(fields__contains=self.value())
        value = self.value()
        if value == 'Music':
            return queryset.filter(fields__contains=Fields.Singer) \
                | queryset.filter(fields__contains=Fields.Rapper) \
                    | queryset.filter(fields__contains=Fields.DJ) \
                    | queryset.filter(fields__contains=Fields.Music_Producer)
        elif value == 'Entertainment':
            return queryset.filter(fields__contains=Fields.Dancer) \
                | queryset.filter(fields__contains=Fields.Streamer) \
                    | queryset.filter(fields__contains=Fields.Content_Creator) \
                    | queryset.filter(fields__contains=Fields.Reviewer) \
                        | queryset.filter(fields__contains=Fields.Blogger)
        elif value == 'Sport':
            return queryset.filter(fields__contains=Fields.Footballer) \
                | queryset.filter(fields__contains=Fields.Gymer_Fitness)
        elif value == 'Financial':
            return queryset.filter(fields__contains=Fields.Investment) \
                | queryset.filter(fields__contains=Fields.Insurance) \
                    | queryset.filter(fields__contains=Fields.Economics_Law) \
                    | queryset.filter(fields__contains=Fields.Capital_Market) \
                        | queryset.filter(fields__contains=Fields.Banking)
        if value:
            return queryset.filter(fields__contains=value)

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

class YearRangeFilter(SimpleListFilter):
    title = 'Year Range' # or use _('country') for translated title
    parameter_name = 'year_range'

    def lookups(self, request, model_admin):
        return (
          ('1', _('Before 1980')),
          ('2', _('1981-1990')),
          ('3', _('1991-2000')),
          ('4', _('After 2000')),
       )

    def queryset(self, request, queryset):
        # to decide how to filter the queryset.
        # return queryset.filter(fields__contains=self.value())
        p1980 = 1980
        p1981 = 1981
        p1990 = 1990
        p1991 = 1991
        p2000 = 2000
        p2001 = 2001
        if self.value() == '1':
            return queryset.filter(year_of_birth__lte=p1980)

        if self.value() == '2':
            return queryset.filter(year_of_birth__gte=p1981, year_of_birth__lte=p1990)
                
        if self.value() == '3':
            return queryset.filter(year_of_birth__gte=p1991, year_of_birth__lte=p2000)
        if self.value() == '4':
            return queryset.filter(year_of_birth__gte=p2001)