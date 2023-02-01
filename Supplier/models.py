# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _
from multiselectfield import MultiSelectField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from .supportmodels import Fields, Location, SupplierChannel, Gender, Kenh
from django.utils.html import format_html

class Supplier(models.Model):
    #no = models.IntegerField() # todo: auto increase
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    channel = models.CharField(max_length=18, choices=SupplierChannel.choices, )
    follower = models.CharField(max_length=20) # 17k -> 17000, 17M -> 17000000 
    follower_2 = models.DecimalField(editable=False, null=True, blank=True, decimal_places=0, max_digits=20,)
    kol_tier = models.CharField(max_length=20, editable=False, null=True, blank=True)

    engagement_rate_percent = models.FloatField(verbose_name='ER(%)', null=True,)
    engagement_rate_absolute = models.FloatField(verbose_name='ER (Ab.)', editable=False, null=True, blank=True)
    engagement_rate_absolute_display = models.CharField(verbose_name='ER (Ab.)', max_length=20, editable=False, null=True, blank=True)

    location = models.CharField(max_length=3, choices=Location.choices, default=Location.SG, )
    year_of_birth = models.IntegerField(
        default=1900,
        validators=[
            MaxValueValidator(2030),
            MinValueValidator(1900)
        ], blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.Male, )
    fields = MultiSelectField(choices=Fields.choices, max_choices=10, max_length=500)
    #ORIGINAL COST
    original_cost_picture = models.DecimalField(verbose_name='ORIGINAL COST - PICTURE', decimal_places=0, max_digits=20, null=True, blank=True)
    original_cost_video = models.DecimalField(verbose_name='ORIGINAL COST - VIDEO', decimal_places=0, max_digits=20, null=True, blank=True)
    original_cost_event = models.DecimalField(verbose_name='ORIGINAL COST - EVENT', decimal_places=0, max_digits=20,  null=True, blank=True)
    original_cost_tvc = models.DecimalField(verbose_name='ORIGINAL COST - TVC', decimal_places=0, max_digits=20, null=True, blank=True)
    kpi = models.CharField(verbose_name='KPI', max_length=50, null=True, blank=True)

    #DISCOUNT, SUPPLIER NAME
    discount = models.CharField(max_length=50, null=True, blank=True)
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
    def year_display(self):
        if self.year_of_birth:
            return "{0}".format(self.year_of_birth)
        return "-"
    year_display.fget.short_description = 'Year'

    
    @property
    def channel_display(self):
        return format_html("<a href='{url}'  target='_blank' >{name}</a>", url=self.link, name=self.channel)
    channel_display.fget.short_description = 'Channel'

    def save(self, *args, **kwargs):
        self.follower_2 = self.follower_value()
        self.kol_tier = self.kol_tier_detect()
        self.engagement_rate_absolute = self.engagement_rate_absolute_calc()
        self.engagement_rate_absolute_display = self.engagement_rate_absolute_display_calc() 
        super(Supplier, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

        
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