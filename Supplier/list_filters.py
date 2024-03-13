from django.contrib.admin import SimpleListFilter
from .models import SupplierModel
from .supportmodels import *
from django.db.models.query import QuerySet
from django.utils.translation import gettext as _

MusicCategory = 'Music', _('1. Music')
EntertainmentCategory = 'Entertainment', _('2. Entertainment')
SportCategory = 'Sport', _('3. Sport')
ArtistCategory = 'Artist', _('4. Artist')
BeautyCategory = 'Beauty', _('5. Beauty')
Life_SocietyCategory = 'Life & SocietyCategory', _('6. Life & Society')
OccupationCategory = 'Occupation', _('7. Occupation')
Property_RealEstateCategory = 'Property & Real estate', _('8. Property & Real estate')
FinancialCategory = 'Financial', _('9. Financial')
FamilyCategory = 'Family', _('10. Family')
AutomotiveCategory = 'Automotive', _('11. Automotive')
FilmProductionCategory = 'Film Production', _('12. Film Production')
Actor_ActressCategory = 'Actor/Actress', _('13. Actor/Actress')
Health_MedicineCategory = 'Health & Medicine', _('14. Health & Medicine')
Youth_GenZCategory = 'Youth & GenZ', _('15. Youth & GenZ')
Media_AdvertisementCategory = 'Media & Advertisement', _('16. Media & Advertisement')
Game_EsportCategory = 'Game & Esport', _('17. Game & Esport')
MC_EditorCategory = 'MC & Editor', _('18. MC & Editor')
Food_DrinkCategory = 'Food & Drink', _('19. Food & Drink')
Technology_EcommerceCategory = 'Technology & Ecommerce', _('20. Technology & Ecommerce')
CelebCategory = 'Celeb', _('21. Celeb')
GeneralCategory = 'General', _('22. General')
OtherCategory = 'Other', _('23. Other')

class IndustryFilter(SimpleListFilter):
    title = 'Industries'
    parameter_name = 'industries'

    def lookups(self, request, model_admin):
        all_choices = Fields.choices
        
        all_Music_fields = []
        all_Entertainment_fields = []
        all_Sport_fields = []
        all_Artist_fields = []
        all_Beauty_fields = []
        all_Life_Society_fields = []
        all_Occupation_fields = []
        all_Property_RealEstate_fields = []
        all_Financial_fields = []
        all_Family_fields = []

        all_Automotive_fields = []
        all_Film_Production_fields = []
        all_Actor_Actress_fields = []
        all_Health_Medicine_fields = []
        all_Youth_GenZ_fields = []
        all_Media_Advertisement_fields = []
        all_Game_Esport_fields = []
        all_MC_Editor_fields = []
        all_Food_Drink_fields = []
        all_Technology_Ecommerce_fields = []
        all_Celeb_fields = []
        all_General_fields = []
        all_Other_fields = []

        for c in all_choices:
            if c[0] in Music_keys():
                all_Music_fields.append(c)
            elif c[0] in Entertainment_keys():
                all_Entertainment_fields.append(c)
            elif c[0] in Sport_keys():
                all_Sport_fields.append(c)
            elif c[0] in Artist_keys():
                all_Artist_fields.append(c)
            if c[0] in Beauty_keys():
                all_Beauty_fields.append(c)
            elif c[0] in Life_Society_keys():
                all_Life_Society_fields.append(c)
            elif c[0] in Occupation_keys():
                all_Occupation_fields.append(c)
            elif c[0] in Property_Real_estate_keys():
                all_Property_RealEstate_fields.append(c)
            if c[0] in Financial_keys():
                all_Financial_fields.append(c)
            elif c[0] in Family_keys():
                all_Family_fields.append(c)
            # elif c[0] in Automotive_keys():
            #     all_Automotive_fields.append(c)
            # if c[0] in Actor_Actress_keys():
            #     all_Actor_Actress_fields.append(c)
            # elif c[0] in Health_Medicine_keys():
            #     all_Health_Medicine_fields.append(c)
            # elif c[0] in Youth_GenZ_keys():
            #     all_Youth_GenZ_fields.append(c)
            # elif c[0] in Media_Advertisement_keys():
            #     all_Media_Advertisement_fields.append(c)
            # elif c[0] in Game_Esport_keys():
            #     all_Game_Esport_fields.append(c)
            # elif c[0] in MC_Editor_keys():
            #     all_MC_Editor_fields.append(c)
            # elif c[0] in Food_Drink_keys():
            #     all_Food_Drink_fields.append(c)
            # elif c[0] in Technology_Ecommerce_keys():
            #     all_Technology_Ecommerce_fields.append(c)
            # elif c[0] in Celeb_keys():
            #     all_Celeb_fields.append(c)
            # elif c[0] in General_keys():
            #     all_General_fields.append(c)
            # elif c[0] in Other_keys():
            #     all_Other_fields.append(c)
            
            
        #t_data = [c.industries for c in SupplierModel.objects.all()]
        result = []

        result.append(MusicCategory)
        for c in all_Music_fields:
            result.append(c)

        result.append(EntertainmentCategory)
        for c in all_Entertainment_fields:
            result.append(c)
        
        result.append(SportCategory)
        for c in all_Sport_fields:
            result.append(c)
        
        result.append(ArtistCategory)
        for c in all_Artist_fields:
            result.append(c)
        
        result.append(BeautyCategory)
        for c in all_Beauty_fields:
            result.append(c)

        result.append(Life_SocietyCategory)
        for c in all_Life_Society_fields:
            result.append(c)

        result.append(OccupationCategory)
        for c in all_Occupation_fields:
            result.append(c)
        result.append(Property_RealEstateCategory)
        for c in all_Property_RealEstate_fields:
            result.append(c)
        result.append(FinancialCategory)
        for c in all_Financial_fields:
            result.append(c)
        result.append(FamilyCategory)
        for c in all_Family_fields:
            result.append(c)
        result.append(AutomotiveCategory)
        for c in all_Automotive_fields:
            result.append(c)

        result.append(FilmProductionCategory)
        for c in all_Film_Production_fields:
            result.append(c)
        
        result.append(Actor_ActressCategory)
        for c in all_Actor_Actress_fields:
            result.append(c)

        result.append(Health_MedicineCategory)
        for c in all_Health_Medicine_fields:
            result.append(c)

        result.append(Youth_GenZCategory)
        for c in all_Youth_GenZ_fields:
            result.append(c)

        result.append(Media_AdvertisementCategory)
        for c in all_Media_Advertisement_fields:
            result.append(c)

        result.append(Game_EsportCategory)
        for c in all_Game_Esport_fields:
            result.append(c)
        result.append(MC_EditorCategory)
        for c in all_MC_Editor_fields:
            result.append(c)
        result.append(Food_DrinkCategory)
        for c in all_Food_Drink_fields:
            result.append(c)
        
        result.append(Technology_EcommerceCategory)
        for c in all_Technology_Ecommerce_fields:
            result.append(c)
        result.append(CelebCategory)
        for c in all_Celeb_fields:
            result.append(c)
        result.append(GeneralCategory)
        for c in all_General_fields:
            result.append(c)
        result.append(OtherCategory)
        for c in all_Other_fields:
            result.append(c)


        # for choice in others_fields:
        #     for t in t_data:
        #         if choice[0] in t:
        #             result.append(choice)
        #             break
        return result

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            
            data = queryset.filter(industries__contains=value)
            if value == MusicCategory[0]:
                for f in Music_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == EntertainmentCategory[0]:
                for f in Entertainment_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == SportCategory[0]:
                for f in Sport_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == ArtistCategory[0]:
                for f in Artist_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == BeautyCategory[0]:
                for f in Beauty_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Life_SocietyCategory[0]:
                for f in Life_Society_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == OccupationCategory[0]:
                for f in Occupation_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Property_RealEstateCategory[0]:
                for f in Property_Real_estate_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == FinancialCategory[0]:
                for f in Financial_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == FamilyCategory[0]:
                for f in Family_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == AutomotiveCategory[0]:
                for f in Automotive_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == FilmProductionCategory[0]:
                for f in Film_Production_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Actor_ActressCategory[0]:
                for f in Actor_Actress_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Health_MedicineCategory[0]:
                for f in Health_Medicine_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Youth_GenZCategory[0]:
                for f in Youth_GenZ_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Media_AdvertisementCategory[0]:
                for f in Media_Advertisement_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Game_EsportCategory[0]:
                for f in Game_Esport_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == MC_EditorCategory[0]:
                for f in MC_Editor_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Food_DrinkCategory[0]:
                for f in Food_Drink_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == Technology_EcommerceCategory[0]:
                for f in Technology_Ecommerce_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == CelebCategory[0]:
                for f in Celeb_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == GeneralCategory[0]:
                for f in General_keys():
                    data = data | queryset.filter(industries__contains=f)
            elif value == OtherCategory[0]:
                for f in Other_keys():
                    data = data | queryset.filter(industries__contains=f)
            
            return data

class FieldsFilter(SimpleListFilter):
    title = 'Fields'
    parameter_name = 'field'

    def lookups(self, request, model_admin):
        MusicKeys = Music_keys()
        EntertainmentKeys = Entertainment_keys()

        SportKeys = Sport_keys()
        FinancialKeys = Financial_keys()

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
            
        t_data = [c.industries for c in SupplierModel.objects.all()]
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
        if value == MusicCategory[0]:
            return queryset.filter(fields__contains=Fields.Singer) \
                | queryset.filter(fields__contains=Fields.Rapper) \
                    | queryset.filter(fields__contains=Fields.DJ) \
                    | queryset.filter(fields__contains=Fields.Music_Producer)
        elif value == EntertainmentCategory[0]:
            return queryset.filter(fields__contains=Fields.Dancer) \
                | queryset.filter(fields__contains=Fields.Streamer) \
                    | queryset.filter(fields__contains=Fields.Content_Creator) \
                    | queryset.filter(fields__contains=Fields.Reviewer) \
                        | queryset.filter(fields__contains=Fields.Blogger)
        elif value == SportCategory[0]:
            return queryset.filter(fields__contains=Fields.Footballer) \
                | queryset.filter(fields__contains=Fields.Gymer_Fitness)
        elif value == FinancialCategory[0]:
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

# class YearRangeFilter(SimpleListFilter):
#     title = 'Year Range' # or use _('country') for translated title
#     parameter_name = 'year_range'

#     def lookups(self, request, model_admin):
#         return (
#           ('1', _('Before 1980')),
#           ('2', _('1981-1990')),
#           ('3', _('1991-2000')),
#           ('4', _('After 2000')),
#        )

#     def queryset(self, request, queryset):
#         # to decide how to filter the queryset.
#         # return queryset.filter(fields__contains=self.value())
#         p1980 = 1980
#         p1981 = 1981
#         p1990 = 1990
#         p1991 = 1991
#         p2000 = 2000
#         p2001 = 2001
#         if self.value() == '1':
#             return queryset.filter(year_of_birth__lte=p1980)

#         if self.value() == '2':
#             return queryset.filter(year_of_birth__gte=p1981, year_of_birth__lte=p1990)
                
#         if self.value() == '3':
#             return queryset.filter(year_of_birth__gte=p1991, year_of_birth__lte=p2000)
#         if self.value() == '4':
#             return queryset.filter(year_of_birth__gte=p2001)

class KPIRangeFilter(SimpleListFilter):
    title = 'KPI'
    parameter_name = 'kpi'

    def lookups(self, request, model_admin):
        return (
          ('1', _('< 10K')),
          ('2', _('10K-50K')),
          ('3', _('50K-100K')),
          ('4', _('100K-500K')),
          ('5', _('500K-1M')),
          ('6', _('>1M')),
          ('7', _('Others')),
       )



    def queryset(self, request, queryset):
        # to decide how to filter the queryset.
        # return queryset.filter(fields__contains=self.value())
        p10 = 10000
        p50 = 50000
        p100 = 100000
        p500 = 500000
        p1M = 1000000
        if self.value() == '1':
            return queryset.filter(kpi_2__gte=0, kpi_2__lt=p10)
        if self.value() == '2':
            return queryset.filter(kpi_2__gte=p10, kpi_2__lt=p50)
                
        if self.value() == '3':
            return queryset.filter(kpi_2__gte=p50, kpi_2__lt=p100)
        if self.value() == '4':
            return queryset.filter(kpi_2__gte=p100, kpi_2__lt=p500)
        if self.value() == '5':
            return queryset.filter(kpi_2__gte=p500, kpi_2__lt=p1M)
        if self.value() == '6':
            return queryset.filter(kpi_2__gte=p1M)
        if self.value() == '7':
            return queryset.filter(kpi_2__lte=-1)
