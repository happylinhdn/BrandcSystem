from queue import Empty
from django.db import models
from django.utils.translation import gettext as _
from multiselectfield import MultiSelectField
from django.conf import settings

class Fields(models.TextChoices):
    Singer = 'Singer', _('Singer')
    Dancer = 'Dancer', _('Dancer')
    Actor_Actress = 'Actor/Actress', _('Actor/Actress')
    Rapper = 'Rapper', _('Rapper')
    DJ = 'DJ', _('DJ')
    Music_Producer = 'Music Producer', _('Music Producer')
    Director = 'Director', _('Director')
    Entertaiment = 'Entertaiment', _('Entertaiment')
    Content_Creator = 'Content Creator', _('Content Creator')
    Gymer_Fitness = 'Gymer/Fitness', _('Gymer/Fitness')
    Teacher_Coach = 'Teacher/ Coach', _('Teacher/ Coach')
    Model = 'Model', _('Model')
    Interior_House = 'Interior house', _('Interior house')
    Footballer = 'Footballer', _('Footballer')

# Create your models here.

# Footballer
# Beauty/Make up
# Cosmestic/Skincare
# Reviewer
# Fashion
# Travel
# Lifestyle
# Real estate
# Sport
# News
# Education
# Insurance
# Hot Mom/Dad
# Freelancer
# Streamer
# Business
# Office staff
# Pet
# Architect
# Smarthome
# Houseware
# Car
# Accomodation
# Office staff
# Game & Esport
# MC & Editor
# Life & Social
# Food & Cooking
# Technology & Ecommerce
# Decor & Design
# Financial & Investment
# Media & Advertisement
# Family & Kid
# Artist & Showbiz
# Health & Medical
# Economics & Law
# Youth & GenZ


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
    engagement_rate_percent = models.CharField(max_length=10)
    location = models.CharField(max_length=3, choices=Location.choices, default=Location.HCM, )
    year_of_birth = models.CharField(max_length=4)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.Male, )
    fields = MultiSelectField(choices=Fields.choices, max_choices=10, max_length=500)
    #ORIGINAL COST
    original_cost_picture = models.CharField(max_length=50, null=True, blank=True)
    original_cost_video = models.CharField(max_length=50, null=True, blank=True)
    original_cost_event = models.CharField(max_length=50, null=True, blank=True)
    kpi = models.CharField(max_length=50, null=True, blank=True)
    #DISCOUNT, SUPPLIER NAME
    discount = models.CharField(max_length=50, null=True, blank=True)
    supplier_name = models.CharField(max_length=100, null=True, blank=True)

    #BOOKING CONTACT: Name, Phone, Email
    booking_contact_name = models.CharField(max_length=100, null=True, blank=True)
    booking_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    booking_contact_email = models.CharField(max_length=50, null=True, blank=True)

    #LATEST UPDATE
    latest_update = models.DateTimeField()
    #HANDLE BY
    handle_by = models.CharField(max_length=100, blank=True)
    #GROUP CHAT NAME
    group_chat_name = models.CharField(max_length=100, blank=True)
    #Kênh (Zalo, Viber or Facebook)
    kenh = models.CharField(max_length=2, choices=Kenh.choices, default=Kenh.Zalo, )
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

    @property
    def kol_tier(self):
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

    def engagement_rate_absolute(self):
        follower_value = self.follower_value()
        rate = 0.0
        try:
            rate = float(self.engagement_rate_percent.replace(",","."))
        except:
            rate = 100
            print("Can not convert engagement_rate_percent")

        return follower_value * rate/100

    @property
    def engagement_rate_absolute_display(self):
        engagement_rate_absolute = self.engagement_rate_absolute()
        if engagement_rate_absolute >= 1000000:
            temp = engagement_rate_absolute/1000000
            return "{0}M".format(round(temp, 2))
        
        if engagement_rate_absolute >= 1000:
            temp = engagement_rate_absolute/1000
            return "{0}K".format(round(temp, 2))
        
        return "{0}".format(round(engagement_rate_absolute, 2))
    
    engagement_rate_absolute_display.fget.short_description = 'Engagement rate absolute'

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