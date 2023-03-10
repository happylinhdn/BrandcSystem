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
    All='To??n Qu???c', _('To??n Qu???c')
    AG='An Giang', _('An Giang')
    BV='B?? R???a-V??ng T??u', _('B?? R???a-V??ng T??u')
    BL='B???c Li??u', _('B???c Li??u')
    BK='B???c K???n', _('B???c K???n')
    BG='B???c Giang', _('B???c Giang')
    BN='B???c Ninh', _('B???c Ninh')
    BT='B???n Tre', _('B???n Tre')
    BD='B??nh D????ng', _('B??nh D????ng')
    B??='B??nh ?????nh', _('B??nh ?????nh')
    BP='B??nh Ph?????c', _('B??nh Ph?????c')
    BTH='B??nh Thu???n', _('B??nh Thu???n')
    CM='C?? Mau', _('C?? Mau')
    CB='Cao B???ng', _('Cao B???ng')
    CT='C???n Th??', _('C???n Th??')
    ??NA='???? N???ng', _('???? N???ng')
    ??L='?????k L???k', _('?????k L???k')
    ??NO='?????k N??ng', _('?????k N??ng')
    ??B='??i???n Bi??n', _('??i???n Bi??n')
    ??N='?????ng Nai', _('?????ng Nai')
    ??T='?????ng Th??p', _('?????ng Th??p')
    GL='Gia Lai', _('Gia Lai')
    HG='H?? Giang', _('H?? Giang')
    HNA='H?? Nam', _('H?? Nam')
    HN='H?? N???i', _('H?? N???i')
    HT='H?? T??nh', _('H?? T??nh')
    HD='H???i D????ng', _('H???i D????ng')
    HP='H???i Ph??ng', _('H???i Ph??ng')
    HGI='H???u Giang', _('H???u Giang')
    HB='H??a B??nh', _('H??a B??nh')
    SG='H??? Ch?? Minh', _('Th??nh ph??? H??? Ch?? Minh')
    HY='H??ng Y??n', _('H??ng Y??n')
    KH='Kh??nh Ho??', _('Kh??nh Ho??')
    KG='Ki??n Giang', _('Ki??n Giang')
    KT='Kon Tum', _('Kon Tum')
    LC='Lai Ch??u', _('Lai Ch??u')
    LS='L???ng S??n', _('L???ng S??n')
    LCA='L??o Cai', _('L??o Cai')
    L??='L??m ?????ng', _('L??m ?????ng')
    ??LA='???? L???t', _('???? L???t')
    LA='Long An', _('Long An')
    N??='Nam ?????nh', _('Nam ?????nh')
    NA='Ngh??? An', _('Ngh??? An')
    NB='Ninh B??nh', _('Ninh B??nh')
    NT='Ninh Thu???n', _('Ninh Thu???n')
    PT='Ph?? Th???', _('Ph?? Th???')
    PY='Ph?? Y??n', _('Ph?? Y??n')
    QB='Qu???ng B??nh', _('Qu???ng B??nh')
    QNA='Qu???ng Nam', _('Qu???ng Nam')
    QNG='Qu???ng Ng??i', _('Qu???ng Ng??i')
    QN='Qu???ng Ninh', _('Qu???ng Ninh')
    QT='Qu???ng Tr???', _('Qu???ng Tr???')
    ST='S??c Tr??ng', _('S??c Tr??ng')
    SL='S??n La', _('S??n La')
    TN='T??y Ninh', _('T??y Ninh')
    TB='Th??i B??nh', _('Th??i B??nh')
    TNG='Th??i Nguy??n', _('Th??i Nguy??n')
    TH='Thanh H??a', _('Thanh H??a')
    TTH='Th???a Thi??n-Hu???', _('Th???a Thi??n-Hu???')
    TG='Ti???n Giang', _('Ti???n Giang')
    TV='Tr?? Vinh', _('Tr?? Vinh')
    TQ='Tuy??n Quang', _('Tuy??n Quang')
    VL='V??nh Long', _('V??nh Long')
    VP='V??nh Ph??c', _('V??nh Ph??c')
    YB='Y??n B??i', _('Y??n B??i')
    NN='N?????c Ngo??i', _('N?????c Ngo??i')

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
    INSTAGRAM = 'Instagram'
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