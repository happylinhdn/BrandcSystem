# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _
from enum import Enum

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
    Cosmestic_Skincare = 'Cosmetic/Skincare', _('Cosmetic/Skincare')
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
    Real_Estate = 'Real estate', _('Real estate')
    Home_Appliance = 'Home appliance', _('Home appliance')
    Interior_House = 'Interior house', _('Interior house')
    Decor_Design = 'Decor & Design', _('Decor & Design')
    Investment = 'Investment', _('Investment')
    Insurance = 'Insurance', _('Insurance')
    Economics_Law = 'Economics & Law', _('Economics & Law')
    Capital_Market  = 'Capital Market', _('Capital Market')
    Banking = 'Banking', _('Banking')
    Kid = 'Kid', _('Kid')
    Hot_Mom_Dad = 'Hot Mom/Dad', _('Hot Mom/Dad')
    Automotive = 'Automotive', _('Automotive')
    Film_Production = 'Film Production', _('Film Production')
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
    Livestream = 'Livestream', _('Livestream')
    Other = 'Other', _('Other')

def Music_keys():
    return [
        Fields.Singer, Fields.Rapper, Fields.DJ, Fields.Music_Producer
    ]

def Entertainment_keys():
    return [
        Fields.Livestream, Fields.Dancer, Fields.Streamer, Fields.Content_Creator, Fields.Reviewer, Fields.Blogger
    ]

def Sport_keys():
    return [Fields.Footballer, Fields.Gymer_Fitness]
def Artist_keys():
    return [ Fields.Model, Fields.Showbiz]
def Beauty_keys():
    return [ Fields.Make_up, Fields.Cosmestic_Skincare]
def Life_Society_keys():
    return [ Fields.Fashion, Fields.Travel, Fields.Lifestyle, Fields.News, Fields.Education]
def Occupation_keys():
    return [ Fields.Teacher_Coach, Fields.Office_staff, Fields.Freelancer, Fields.Business, Fields.Lawyer, Fields.Student, Fields.Doctor]

def Property_Real_estate_keys():
    return [ Fields.Architect, Fields.Smarthome, Fields.Home_Appliance, Fields.Interior_House, Fields.Decor_Design, Fields.Real_Estate]

def Property_Real_estate_keys():
    return [ Fields.Architect, Fields.Smarthome, Fields.Home_Appliance, Fields.Interior_House, Fields.Decor_Design, Fields.Real_Estate]

def Financial_keys():
    return [
        Fields.Investment, Fields.Insurance, Fields.Economics_Law, Fields.Capital_Market, Fields.Banking
    ]

def Family_keys():
    return [ Fields.Kid, Fields.Hot_Mom_Dad]

def Automotive_keys():
    return [ Fields.Automotive]
def Film_Production_keys():
    return [ Fields.Film_Production]
def Actor_Actress_keys():
    return [ Fields.Actor_Actress]
def Health_Medicine_keys():
    return [ Fields.Health_Medicine]
def Youth_GenZ_keys():
    return [ Fields.Youth_GenZ]
def Media_Advertisement_keys():
    return [ Fields.Media_Advertisement]
def Game_Esport_keys():
    return [ Fields.Game_Esport]
def MC_Editor_keys():
    return [ Fields.MC_Editor]

def Food_Drink_keys():
    return [ Fields.Food_Drink]

def Technology_Ecommerce_keys():
    return [ Fields.Technology_Ecommerce]
def Celeb_keys():
    return [ Fields.Celeb]
def General_keys():
    return [ Fields.General]
def Other_keys():
    return [ Fields.Other]

class Location(models.TextChoices):
    All='Toàn Quốc', _('Toàn Quốc')
    AG='An Giang', _('An Giang')
    BV='Bà Rịa-Vũng Tàu', _('Bà Rịa-Vũng Tàu')
    BL='Bạc Liêu', _('Bạc Liêu')
    BK='Bắc Kạn', _('Bắc Kạn')
    BG='Bắc Giang', _('Bắc Giang')
    BN='Bắc Ninh', _('Bắc Ninh')
    BT='Bến Tre', _('Bến Tre')
    BD='Bình Dương', _('Bình Dương')
    BĐ='Bình Định', _('Bình Định')
    BP='Bình Phước', _('Bình Phước')
    BTH='Bình Thuận', _('Bình Thuận')
    CM='Cà Mau', _('Cà Mau')
    CB='Cao Bằng', _('Cao Bằng')
    CT='Cần Thơ', _('Cần Thơ')
    ĐNA='Đà Nẵng', _('Đà Nẵng')
    ĐL='Đắk Lắk', _('Đắk Lắk')
    ĐNO='Đắk Nông', _('Đắk Nông')
    ĐB='Điện Biên', _('Điện Biên')
    ĐN='Đồng Nai', _('Đồng Nai')
    ĐT='Đồng Tháp', _('Đồng Tháp')
    GL='Gia Lai', _('Gia Lai')
    HG='Hà Giang', _('Hà Giang')
    HNA='Hà Nam', _('Hà Nam')
    HN='Hà Nội', _('Hà Nội')
    HT='Hà Tĩnh', _('Hà Tĩnh')
    HD='Hải Dương', _('Hải Dương')
    HP='Hải Phòng', _('Hải Phòng')
    HGI='Hậu Giang', _('Hậu Giang')
    HB='Hòa Bình', _('Hòa Bình')
    SG='Hồ Chí Minh', _('Thành phố Hồ Chí Minh')
    HY='Hưng Yên', _('Hưng Yên')
    KH='Khánh Hòa', _('Khánh Hòa')
    KG='Kiên Giang', _('Kiên Giang')
    KT='Kon Tum', _('Kon Tum')
    LC='Lai Châu', _('Lai Châu')
    LS='Lạng Sơn', _('Lạng Sơn')
    LCA='Lào Cai', _('Lào Cai')
    LĐ='Lâm Đồng', _('Lâm Đồng')
    ĐLA='Đà Lạt', _('Đà Lạt')
    LA='Long An', _('Long An')
    NĐ='Nam Định', _('Nam Định')
    NA='Nghệ An', _('Nghệ An')
    NB='Ninh Bình', _('Ninh Bình')
    NT='Ninh Thuận', _('Ninh Thuận')
    PT='Phú Thọ', _('Phú Thọ')
    PY='Phú Yên', _('Phú Yên')
    QB='Quảng Bình', _('Quảng Bình')
    QNA='Quảng Nam', _('Quảng Nam')
    QNG='Quảng Ngãi', _('Quảng Ngãi')
    QN='Quảng Ninh', _('Quảng Ninh')
    QT='Quảng Trị', _('Quảng Trị')
    ST='Sóc Trăng', _('Sóc Trăng')
    SL='Sơn La', _('Sơn La')
    TN='Tây Ninh', _('Tây Ninh')
    TB='Thái Bình', _('Thái Bình')
    TNG='Thái Nguyên', _('Thái Nguyên')
    TH='Thanh Hóa', _('Thanh Hóa')
    TTH='Thừa Thiên-Huế', _('Thừa Thiên-Huế')
    TG='Tiền Giang', _('Tiền Giang')
    TV='Trà Vinh', _('Trà Vinh')
    TQ='Tuyên Quang', _('Tuyên Quang')
    VL='Vĩnh Long', _('Vĩnh Long')
    VP='Vĩnh Phúc', _('Vĩnh Phúc')
    YB='Yên Bái', _('Yên Bái')
    NN='Nước Ngoài', _('Nước Ngoài')

class SupplierChannel(models.TextChoices):
    FB_GROUP = 'Facebook Group', _('Facebook Group')
    FB_FANPAGE = 'Facebook Fanpage', _('Facebook Fanpage')
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

class XPATH(Enum):
    FB_FANPAGE_1 = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[5]/div/div/div/div[2]/div/div/span/span'
    FB_FANPAGE_2 = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]'
    FB_GROUP = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/span/span/div/div[3]/a'
    #LeBaoBinh - OK
    FB_PERSONAL_1 = '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]' 
    TIKTOK_PERSONAL = '/html/body/div[2]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong'
    TIKTOK_COMMUNITY = '/html/body/div[2]/div[2]/div[2]/div/div[1]/h3/div[2]/strong'
    YOUTUBE_COMMUNITY = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string[2]'
    #Todo: let check HoQuangHieu - need login?
    FB_PERSONAL_2 = '//*[@id="mount_0_0_4z"]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[1] ' 
    #Not ready
    YOUTUBE_PERSONAL = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string[2]'
    INSTAGRAM = '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/button/div'
    FORUM = 'Forum'
    WEBSITE = 'Website'
    LINKED_IN = 'Linkedin'
    OTHERS = 'Others'


class Gender(models.TextChoices):
    Male = 'Male', _('Male')
    Female = 'Female', _('Female')
    General='General', _('General')

class Kenh(models.TextChoices):
    Zalo = 'Zalo', _('Zalo')
    Viber = 'Viber', _('Viber')
    Facebook = 'Facebook', _('Facebook')

#######Utility
def support_sync(channel):
    supports = [
        SupplierChannel.FB_GROUP,
        SupplierChannel.FB_FANPAGE,
        SupplierChannel.FB_PERSONAL,
        SupplierChannel.TIKTOK_COMMUNITY,
        SupplierChannel.TIKTOK_PERSONAL,
        SupplierChannel.YOUTUBE_COMMUNITY,
        SupplierChannel.YOUTUBE_PERSONAL,
        SupplierChannel.INSTAGRAM
    ]
    if channel in supports:
        return True

    return False

def isFbChannel(channel):
    supports = [
        SupplierChannel.FB_GROUP,
        SupplierChannel.FB_FANPAGE,
        SupplierChannel.FB_PERSONAL
    ]
    if channel in supports:
        return True

    return False

class YearCategory(models.TextChoices):
    GenZ = 'Gen Z (1997 - 2012)', _('Gen Z (1997 - 2012)')
    GenY = 'Gen Y (1981 - 1996)', _('Gen Y (1981 - 1996)')
    GenX = 'Gen X (1965 - 1980)', _('Gen X (1965 - 1980)')
    General = 'General', _('General')