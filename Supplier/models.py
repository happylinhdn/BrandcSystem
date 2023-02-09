# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _
from multiselectfield import MultiSelectField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from .supportmodels import Fields, Location, SupplierChannel, Gender, Kenh
from django.contrib import messages


class Supplier(models.Model):
    #no = models.IntegerField() # todo: auto increase
    name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=300, null=True)
    channel = models.CharField(max_length=18, choices=SupplierChannel.choices, null=True)
    follower = models.CharField(max_length=20) # 17k -> 17000, 17M -> 17000000 
    follower_2 = models.DecimalField(editable=False, null=True, decimal_places=0, max_digits=20,)
    kol_tier = models.CharField(max_length=20, editable=False, null=True)
    
    engagement_rate_percent = models.FloatField(verbose_name='ER(%)', null=True,)
    engagement_rate_absolute = models.FloatField(verbose_name='ER (Ab.)', editable=False, null=True)

    location = models.CharField(max_length=20, choices=Location.choices, null=True )
    year_of_birth = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(2030),
            MinValueValidator(1900)
        ])
    gender = models.CharField(max_length=6, choices=Gender.choices, null=True)
    
    fields = MultiSelectField(choices=Fields.choices, max_choices=10, max_length=500, null=True)
    #ORIGINAL COST
    original_cost_picture = models.DecimalField(verbose_name='Org. cost - Picture', decimal_places=0, max_digits=20, null=True)
    original_cost_video = models.DecimalField(verbose_name='Org. cost - Video', decimal_places=0, max_digits=20, null=True)
    original_cost_event = models.DecimalField(verbose_name='Org. cost - Event', decimal_places=0, max_digits=20,  null=True)
    original_cost_tvc = models.DecimalField(verbose_name='Org. cost - TVC', decimal_places=0, max_digits=20, null=True)
    kpi = models.CharField(verbose_name='KPI', max_length=50, null=True)

    #DISCOUNT, SUPPLIER NAME
    discount = models.CharField(max_length=50, null=True)
    supplier_name = models.CharField(max_length=100, null=True)

    #BOOKING CONTACT: Name, Phone, Email
    booking_contact_name = models.CharField(max_length=100, null=True)
    booking_contact_phone = models.CharField(max_length=15, null=True)
    booking_contact_email = models.CharField(max_length=50, null=True)

    #profile = models.FileField(verbose_name='PROFILE/QUOTATION', upload_to="profile", null=True, blank=True)
    profile = models.CharField(verbose_name='Profile/Quatation', max_length=300, null=True)

    latest_update = models.DateTimeField(null=True)
    #HANDLE BY
    handle_by = models.CharField(max_length=100, null=True)
    #GROUP CHAT NAME
    group_chat_name = models.CharField(max_length=100, null=True)
    #Kênh (Zalo, Viber or Facebook) 
    group_chat_channel = models.CharField(verbose_name='Group Chat Channel', max_length=8, choices=Kenh.choices, null=True)
    #Set Leader Mode to Ms. Lana
    lana_leader = models.BooleanField(default = False, null=True)
    #History
    history = models.DateTimeField(auto_now_add=True, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


    def follower_value(self):
        follower = str(self.follower) or '0'
        upperFollower = follower.upper().replace(",",".")
        value = 0
        if 'K' in upperFollower:
            tempK = upperFollower.split("K")
            try:
                value = float(tempK[0]) * 1000
            except:
                print("Can not convert follower thousands")
                raise Exception("The value of follower is not valid: " + str(self.follower  or ''))

        elif 'M' in upperFollower:
            tempK = upperFollower.split("M")
            try:
                value = float(tempK[0]) * 1000000
            except:
                print("Can not convert follower million")
                raise Exception("The value of follower is not valid: " + str(self.follower  or ''))
        else:
            try:
                value = float(upperFollower)
            except:
                value = 0
                raise Exception("The value of follower is not valid: " + str(self.follower  or ''))
        
        return value

    def kol_tier_detect(self):
        if self.follower_2 in range(0, 10000):
            return "Nano influencer"
        elif self.follower_2 in range(10000, 50000):
            return "Micro influencer"
        elif self.follower_2 in range(50000, 500000):
            return "Mid tier influencer"
        elif self.follower_2 in range(500000, 1000000):
            return "Macro influencer"
        elif self.follower_2 >= 1000000:
            return "Mega influencer"
        else:
            return "Unknown"

    def engagement_rate_absolute_calc(self):
        follower_value = self.follower_2
        rate = 0.0
        try:
            rate = self.engagement_rate_percent or 0
        except:
            rate = 100
            print("Can not convert engagement_rate_percent")

        return follower_value * rate/100

    def engagement_rate_absolute_display_calc(self):
        if self.engagement_rate_absolute >= 1000000:
            temp = self.engagement_rate_absolute/1000000
            return "{0}M".format(round(temp, 2))
        
        if self.engagement_rate_absolute >= 1000:
            temp = self.engagement_rate_absolute/1000
            return "{0}K".format(round(temp, 2))
        
        return "{0}".format(round(self.engagement_rate_absolute, 2))


    def save(self, *args, **kwargs):
        self.valid_form()
        super(Supplier, self).save(*args, **kwargs)
    
    def valid_form(self):
        self.follower_2 = self.follower_value()
        self.kol_tier = self.kol_tier_detect()
        self.engagement_rate_absolute = self.engagement_rate_absolute_calc() 
        
        if self.location:
            self.location = self.location.strip()

        if self.location == 'Vũng Tàu':
            self.location = 'Bà Rịa-Vũng Tàu'
        
        if self.location is None:
            raise Exception('Location can not empty')
    
        if self.location not in (key[0] for key in Location.choices):
            raise Exception('Location is not valid: ' + str(self.location or ''))

        if self.fields is None:
            raise Exception('Fields can not empty')
        
        if self.fields and type(self.fields) == str:
            valid = []
            fields = (f.strip() for f in self.fields.split(",")) 
            all_fields = Fields.choices

            for field in fields:
                if field and field not in (key[0] for key in all_fields):
                    print('Field is not valid:' + str(field or ''))
                    raise Exception('Field is not valid:' + str(field or ''))
                else:
                    valid.append(field)
            self.fields = ','.join(valid)
        
        if self.channel is None:
            raise Exception('Channel can not empty')

        if self.channel:
            self.channel = self.channel.strip()
        
        if self.channel and self.channel not in (key[0] for key in SupplierChannel.choices):
            raise Exception('Channel is not valid: ' + str(self.channel or ''))

        if self.gender is None:
            raise Exception('Gender can not empty')

        if self.gender:
            self.gender = self.gender.strip()

        if self.gender and self.gender not in (key[0] for key in Gender.choices):
            raise Exception('Gender is not valid: ' + str(self.gender or ''))
        

    def __str__(self):
        return self.name

        
    def parse_to_json(self):
        return {
            'id': self.id,
            'NAME': self.name,
            'LINK': self.link,
            'CHANNEL': self.channel,
            'FOLLOWER': self.follower,
            'KOL TIER': self.kol_tier,
            'ER(%)': self.engagement_rate_percent,
            'ER (Ab.)': self.engagement_rate_absolute_display_calc(),
            'LOCATION': self.location,
            'YEAR': self.year_of_birth,
            'GENDER': self.gender,
            'FIELDS': self.fields,
            'ORIGINAL COST - PICTURE': int(self.original_cost_picture or 0),
            'ORIGINAL COST - VIDEO':int(self.original_cost_video or 0),
            'ORIGINAL COST - EVENT': int(self.original_cost_event or 0),
            'ORIGINAL COST - TVC':int(self.original_cost_tvc or 0),
            'KPI': self.kpi,
            'DISCOUNT': self.discount,
            'SUPPLIER NAME': self.supplier_name,
            'BOOKING CONTACT NAME': self.booking_contact_name,
            'BOOKING CONTACT PHONE': self.booking_contact_phone,
            'BOOKING CONTACT EMAIL': self.booking_contact_email,
            'PROFILE/QUOTATION': self.profile,
            'LATEST UPDATE': self.latest_update.strftime('%Y-%m-%d %H:%M'),
            'HANDLE BY': self.handle_by,
            'GROUP CHAT NAME': self.group_chat_name,
            'GROUP CHAT CHANNEL': self.group_chat_channel,
            'LANE LEADER': self.lana_leader,
            'MODIFIED BY': self.modified_by
        }

    class Meta:
        permissions = [
            ("import_data_as_admin", "Can import data"),
            ("export_excel_50_seller", "Can export excel as a seller role (50)"),
            ("export_excel_100_buyer", "Can export excel as a buyer role (100)"),
            ("export_excel_1000_admin", "Can export excel as an admin role"),
            ("sync_follower", "Can sync follower number of kol")
        ]

class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")