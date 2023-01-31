# -*- coding: utf-8 -*-
from queue import Empty
from django.db import models
from django.utils.translation import gettext as _
from multiselectfield import MultiSelectField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Fields(models.TextChoices):
    Singer = 'Singer', _('Singer')
    Rapper = 'Rapper', _('Rapper')
    DJ = 'DJ', _('DJ')
    Music_Producer = 'Music Producer', _('Music Producer')
    Dancer = 'Dancer', _('Dancer')
    Streamer = 'Streamer', _('Streamer')
    Content_Creator = 'Content Creator', _('Content Creator')
    Reviewer = 'Reviewer', _('Reviewer')
    Footballer = 'Footballer', _('Footballer')
    Gymer_Fitness = 'Gymer/Fitness', _('Gymer/Fitness')
    Model = 'Model', _('Model')
    Showbiz = 'Showbiz', _('Showbiz')
    Make_up = 'Make-up', _('Make-up')
    Cosmestic_Skincare = 'Cosmestic/Skincare', _('Cosmestic/Skincare')
    Fashion = 'Fashion', _('Fashion')
    Travel = 'Travel', _('Travel')
    Lifestyle = 'Lifestyle', _('Lifestyle')
    News = 'News', _('News')
    Education = 'Education', _('Education')
    Teacher_Coach = 'Teacher/Coach', _('Teacher/Coach')
    Office_staff = 'Office staff', _('Office staff')
    Freelancer = 'Freelancer', _('Freelancer')
    Business = 'Business', _('Business')
    Architect = 'Architect', _('Architect')
    Smarthome = 'Smarthome', _('Smarthome')
    Home_Appliance = 'Home appliance', _('Home appliance')
    Interior_House = 'Interior house', _('Interior house')
    Decor_Design = 'Decor & Design', _('Decor & Design')
    Investment = 'Investment', _('Investment')
    Insurance = 'Insurance', _('Insurance')
    Economics_Law = 'Economics & Law', _('Economics & Law')
    Capital_Market  = 'Capital Market ', _('Capital Market ')
    Banking = 'Banking', _('Banking')
    Kid = 'Kid', _('Kid')
    Hot_Mom_Dad = 'Hot Mom/Dad', _('Hot Mom/Dad')
    Automotive = 'Automotive', _('Automotive')
    Director = 'Director', _('Director')
    Actor_Actress = 'Actor/Actress', _('Actor/Actress')
    Health_Medicine = 'Health & Medicine', _('Health & Medicine')
    Youth_GenZ = 'Youth & GenZ', _('Youth & GenZ')
    Media_Advertisement = 'Media & Advertisement', _('Media & Advertisement')
    Game_Esport = 'Game & Esport', _('Game & Esport')
    MC_Editor = 'MC & Editor', _('MC & Editor')
    Food_Drink = 'Food & Drink', _('Food & Drink')
    Technology_Ecommerce = 'Technology & Ecommerce', _('Technology & Ecommerce')
    Celeb = 'Celeb', _('Celeb')
    General = 'General', _('General')
    Other = 'Other', _('Other')
    
class SupplierChannel(models.TextChoices):
    FB_COMMUNITY = 'Facebook Community', _('Facebook Community')
    FB_PERSONAL = 'Facebook Personal', _('Facebook Personal')
    TIKTOK_COMMUNITY = 'Tiktok Community', _('Tiktok Community')
    TIKTOK_PERSONAL = 'Tiktok Personal', _('Tiktok Personal')
    YOUTUBE_COMMUNITY = 'Youtube Community', _('Youtube Community')
    YOUTUBE_PERSONAL = 'Youtube Personal', _('Youtube Personal')
    INSTAGRAM = 'Instagram', _('Instagram')
    FORUM = 'Forum', _('Forum')
    WEBSITE = 'Website', _('Website')
    LINKED_IN = 'Linkedin', _('Linkedin')
    OTHERS = 'Others', _('Others')

class Location(models.TextChoices):
    HCM = 'HCM', _('Hồ Chí Minh')
    HN = 'HN', _('Hà Nội')

class Gender(models.TextChoices):
    Male = 'Ma', _('Male')
    Female = 'Fe', _('Female')

class Kenh(models.TextChoices):
    Zalo = 'za', _('Zalo')
    Viber = 'vi', _('Viber')
    Facebook = 'fb', _('Facebook')

class Supplier(models.Model):
    #no = models.IntegerField() # todo: auto increase
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    channel = models.CharField(max_length=18, choices=SupplierChannel.choices, )
    follower = models.CharField(max_length=20) # 17k -> 17000, 17M -> 17000000 
    follower_2 = models.FloatField(editable=False, null=True, blank=True)
    kol_tier = models.CharField(max_length=20, editable=False, null=True, blank=True)

    engagement_rate_percent = models.FloatField(verbose_name='ER(%)', max_length=10)
    engagement_rate_absolute = models.FloatField(verbose_name='ER (Ab.)', max_length=20, editable=False, null=True, blank=True)
    engagement_rate_absolute_display = models.CharField(verbose_name='ER (Ab.)', max_length=20, editable=False, null=True, blank=True)

    location = models.CharField(max_length=3, choices=Location.choices, default=Location.HCM, )
    year_of_birth = models.IntegerField(
        default=1900,
        validators=[
            MaxValueValidator(2030),
            MinValueValidator(1900)
        ], blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.Male, )
    fields = MultiSelectField(choices=Fields.choices, max_choices=10, max_length=500)
    #ORIGINAL COST
    original_cost_picture = models.FloatField(verbose_name='ORIGINAL COST - PICTURE', null=True, blank=True)
    original_cost_video = models.FloatField(verbose_name='ORIGINAL COST - VIDEO', null=True, blank=True)
    original_cost_event = models.FloatField(verbose_name='ORIGINAL COST - EVENT',  null=True, blank=True)
    original_cost_tvc = models.FloatField(verbose_name='ORIGINAL COST - TVC', null=True, blank=True)
    kpi = models.FloatField(verbose_name='KPI',max_length=50, null=True, blank=True)

    #DISCOUNT, SUPPLIER NAME
    discount = models.FloatField(max_length=50, null=True, blank=True)
    supplier_name = models.CharField(max_length=100, null=True, blank=True)

    #BOOKING CONTACT: Name, Phone, Email
    booking_contact_name = models.CharField(max_length=100, null=True, blank=True)
    booking_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    booking_contact_email = models.CharField(max_length=50, null=True, blank=True)

    profile_quotation = models.CharField(verbose_name='PROFILE/QUOTATION', max_length=50, null=True, blank=True)
    latest_update = models.DateTimeField()
    #HANDLE BY
    handle_by = models.CharField(max_length=100, blank=True)
    #GROUP CHAT NAME
    group_chat_name = models.CharField(max_length=100, blank=True)
    #Kênh (Zalo, Viber or Facebook) 
    group_chat_channel = models.CharField(verbose_name='Group Chat Channel', max_length=2, choices=Kenh.choices, default=Kenh.Zalo, )
    #Set Leader Mode to Ms. Lana
    lana_leader = models.BooleanField(default=False)
    #History
    history = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


    def follower_value(self):
        upperFollower = self.follower.upper().replace(",",".")
        value = 0
        if 'K' in upperFollower:
            tempK = upperFollower.split("K")
            try:
                value = float(tempK[0]) * 1000
            except:
                print("Can not convert follower thousands")

        elif 'M' in upperFollower:
            tempK = upperFollower.split("M")
            try:
                value = float(tempK[0]) * 1000000
            except:
                print("Can not convert follower million")
        else:
            try:
                value = float(upperFollower)
            except:
                print("Can not convert follower")
        return value

    def kol_tier_detect(self):
        if self.follower_value() in range(1, 10000):
            return "Nano influencer"
        elif self.follower_value() in range(10000, 50000):
            return "Micro influencer"
        elif self.follower_value() in range(50000, 500000):
            return "Mid tier influencer"
        elif self.follower_value() in range(500000, 1000000):
            return "Macro influencer"
        elif self.follower_value() >= 1000000:
            return "Mega influencer"
        else:
            return "Unknown"

    def engagement_rate_absolute_calc(self):
        follower_value = self.follower_value()
        rate = 0.0
        try:
            rate = self.engagement_rate_percent
        except:
            rate = 100
            print("Can not convert engagement_rate_percent")

        return follower_value * rate/100

    def engagement_rate_absolute_display_calc(self):
        engagement_rate_absolute = self.engagement_rate_absolute_calc()
        if engagement_rate_absolute >= 1000000:
            temp = engagement_rate_absolute/1000000
            return "{0}M".format(round(temp, 2))
        
        if engagement_rate_absolute >= 1000:
            temp = engagement_rate_absolute/1000
            return "{0}K".format(round(temp, 2))
        
        return "{0}".format(round(engagement_rate_absolute, 2))

    @property
    def booking_contact_display(self):
        return """Name:{0} - Phone: {1} - Email:{2}""".format(self.booking_contact_name, self.booking_contact_phone, self.booking_contact_email)

    booking_contact_display.fget.short_description = 'Booking contact'

    def save(self, *args, **kwargs):
        self.follower_2 = self.follower_value()
        self.kol_tier = self.kol_tier_detect()
        self.engagement_rate_absolute = self.engagement_rate_absolute_calc()
        self.engagement_rate_absolute_display = self.engagement_rate_absolute_display_calc() 

        all_choices = Fields.choices
        t_data = [c.fields for c in Supplier.objects.all()]
        result = ()
        for choice in all_choices:
            print(choice[1])
            # for t in t_data:
            #     if choice.value() in t:
            #         result.append(choice)
            #         break

        super(Supplier, self).save(*args, **kwargs)

        
    def parse_to_json(self):
        return {
            'name': self.name,
            'link': self.link,
            'channel': self.channel,
            'follower': self.follower,
            'engagement_rate_percent': self.engagement_rate_percent,
            'location': self.location,
            'year_of_birth': self.year_of_birth,
            'gender': self.gender,
            'fields': self.fields,
            'original_cost_picture': self.original_cost_picture,
            'original_cost_video':self.original_cost_video,
            'original_cost_event':self.original_cost_event,
            'kpi': self.kpi,
            'discount': self.discount,
            'supplier_name': self.supplier_name,
            'booking_contact_name': self.booking_contact_name,
            'booking_contact_phone': self.booking_contact_phone,
            'booking_contact_email': self.booking_contact_email,
            'latest_update': self.latest_update.strftime('%Y-%m-%d %H:%M'),
            'handle_by': self.handle_by,
            'group_chat_name': self.group_chat_name,
            'kenh': self.kenh,
            'lana_leader': self.lana_leader
        }


class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")