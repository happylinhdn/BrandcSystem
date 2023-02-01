# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _

class Fields(models.TextChoices):
    Singer = 'Singer', _('Singer')
    Rapper = 'Rapper', _('Rapper')
    DJ = 'DJ', _('DJ')
    Music_Producer = 'Music Producer', _('Music Producer')
    Dancer = 'Dancer', _('Dancer')
    Streamer = 'Streamer', _('Streamer')
    Content_Creator = 'Content Creator', _('Content Creator')
    Reviewer = 'Reviewer', _('Reviewer')
    Blogger = 'Blogger', _('Blogger')
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
    Lawyer = 'Lawyer', _('Lawyer')
    Student = 'Student', _('Student')
    Doctor = 'Doctor', _('Doctor')
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

class Location(models.TextChoices):
    AG='AG', _('An Giang')
    BV='BV', _('Bà Rịa-Vũng Tàu')
    BL='BL', _('Bạc Liêu')
    BK='BK', _('Bắc Kạn')
    BG='BG', _('Bắc Giang')
    BN='BN', _('Bắc Ninh')
    BT='BT', _('Bến Tre')
    BD='BD', _('Bình Dương')
    BĐ='BĐ', _('Bình Định')
    BP='BP', _('Bình Phước')
    BTH='BTH', _('Bình Thuận')
    CM='CM', _('Cà Mau')
    CB='CB', _('Cao Bằng')
    CT='CT', _('Cần Thơ')
    ĐNA='ĐNA', _('Đà Nẵng')
    ĐL='ĐL', _('Đắk Lắk')
    ĐNO='ĐNO', _('Đắk Nông')
    ĐB='ĐB', _('Điện Biên')
    ĐN='ĐN', _('Đồng Nai')
    ĐT='ĐT', _('Đồng Tháp')
    GL='GL', _('Gia Lai')
    HG='HG', _('Hà Giang')
    HNA='HNA', _('Hà Nam')
    HN='HN', _('Hà Nội')
    HT='HT', _('Hà Tĩnh')
    HD='HD', _('Hải Dương')
    HP='HP', _('Hải Phòng')
    HGI='HGI', _('Hậu Giang')
    HB='HB', _('Hòa Bình')
    SG='SG', _('Thành phố Hồ Chí Minh')
    HY='HY', _('Hưng Yên')
    KH='KH', _('Khánh Hoà')
    KG='KG', _('Kiên Giang')
    KT='KT', _('Kon Tum')
    LC='LC', _('Lai Châu')
    LS='LS', _('Lạng Sơn')
    LCA='LCA', _('Lào Cai')
    LĐ='LĐ', _('Lâm Đồng')
    LA='LA', _('Long An')
    NĐ='NĐ', _('Nam Định')
    NA='NA', _('Nghệ An')
    NB='NB', _('Ninh Bình')
    NT='NT', _('Ninh Thuận')
    PT='PT', _('Phú Thọ')
    PY='PY', _('Phú Yên')
    QB='QB', _('Quảng Bình')
    QNA='QNA', _('Quảng Nam')
    QNG='QNG', _('Quảng Ngãi')
    QN='QN', _('Quảng Ninh')
    QT='QT', _('Quảng Trị')
    ST='ST', _('Sóc Trăng')
    SL='SL', _('Sơn La')
    TN='TN', _('Tây Ninh')
    TB='TB', _('Thái Bình')
    TNG='TNG', _('Thái Nguyên')
    TH='TH', _('Thanh Hóa')
    TTH='TTH', _('Thừa Thiên-Huế')
    TG='TG', _('Tiền Giang')
    TV='TV', _('Trà Vinh')
    TQ='TQ', _('Tuyên Quang')
    VL='VL', _('Vĩnh Long')
    VP='VP', _('Vĩnh Phúc')
    YB='YB', _('Yên Bái')

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

class Gender(models.TextChoices):
    Male = 'Ma', _('Male')
    Female = 'Fe', _('Female')

class Kenh(models.TextChoices):
    Zalo = 'za', _('Zalo')
    Viber = 'vi', _('Viber')
    Facebook = 'fb', _('Facebook')