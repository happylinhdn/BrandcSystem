# Generated by Django 4.1.5 on 2023-02-06 07:55

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0046_alter_supplier_group_chat_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='channel',
            field=models.CharField(choices=[('Facebook Group', 'Facebook Group'), ('Facebook Fanpage', 'Facebook Fanpage'), ('Facebook Personal', 'Facebook Personal'), ('Tiktok Community', 'Tiktok Community'), ('Tiktok Personal', 'Tiktok Personal'), ('Youtube Community', 'Youtube Community'), ('Youtube Personal', 'Youtube Personal'), ('Instagram', 'Instagram'), ('Forum', 'Forum'), ('Website', 'Website'), ('Linkedin', 'Linkedin'), ('Others', 'Others')], max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='fields',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Singer', 'Singer'), ('Rapper', 'Rapper'), ('DJ', 'DJ'), ('Music Producer', 'Music Producer'), ('Dancer', 'Dancer'), ('Streamer', 'Streamer'), ('Content Creator', 'Content Creator'), ('Reviewer', 'Reviewer'), ('Blogger', 'Blogger'), ('Footballer', 'Footballer'), ('Gymer/Fitness', 'Gymer/Fitness'), ('Model', 'Model'), ('Showbiz', 'Showbiz'), ('Make-up', 'Make-up'), ('Cosmestic/Skincare', 'Cosmestic/Skincare'), ('Fashion', 'Fashion'), ('Travel', 'Travel'), ('Lifestyle', 'Lifestyle'), ('News', 'News'), ('Education', 'Education'), ('Teacher/Coach', 'Teacher/Coach'), ('Office staff', 'Office staff'), ('Freelancer', 'Freelancer'), ('Business', 'Business'), ('Lawyer', 'Lawyer'), ('Student', 'Student'), ('Doctor', 'Doctor'), ('Architect', 'Architect'), ('Smarthome', 'Smarthome'), ('Home appliance', 'Home appliance'), ('Interior house', 'Interior house'), ('Decor & Design', 'Decor & Design'), ('Investment', 'Investment'), ('Insurance', 'Insurance'), ('Economics & Law', 'Economics & Law'), ('Capital Market ', 'Capital Market '), ('Banking', 'Banking'), ('Kid', 'Kid'), ('Hot Mom/Dad', 'Hot Mom/Dad'), ('Automotive', 'Automotive'), ('Director', 'Director'), ('Actor/Actress', 'Actor/Actress'), ('Health & Medicine', 'Health & Medicine'), ('Youth & GenZ', 'Youth & GenZ'), ('Media & Advertisement', 'Media & Advertisement'), ('Game & Esport', 'Game & Esport'), ('MC & Editor', 'MC & Editor'), ('Food & Drink', 'Food & Drink'), ('Technology & Ecommerce', 'Technology & Ecommerce'), ('Celeb', 'Celeb'), ('General', 'General'), ('Other', 'Other')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='group_chat_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='handle_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='history',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='latest_update',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='location',
            field=models.CharField(choices=[('An Giang', 'An Giang'), ('B?? R???a-V??ng T??u', 'B?? R???a-V??ng T??u'), ('B???c Li??u', 'B???c Li??u'), ('B???c K???n', 'B???c K???n'), ('B???c Giang', 'B???c Giang'), ('B???c Ninh', 'B???c Ninh'), ('B???n Tre', 'B???n Tre'), ('B??nh D????ng', 'B??nh D????ng'), ('B??nh ?????nh', 'B??nh ?????nh'), ('B??nh Ph?????c', 'B??nh Ph?????c'), ('B??nh Thu???n', 'B??nh Thu???n'), ('C?? Mau', 'C?? Mau'), ('Cao B???ng', 'Cao B???ng'), ('C???n Th??', 'C???n Th??'), ('???? N???ng', '???? N???ng'), ('?????k L???k', '?????k L???k'), ('?????k N??ng', '?????k N??ng'), ('??i???n Bi??n', '??i???n Bi??n'), ('?????ng Nai', '?????ng Nai'), ('?????ng Th??p', '?????ng Th??p'), ('Gia Lai', 'Gia Lai'), ('H?? Giang', 'H?? Giang'), ('H?? Nam', 'H?? Nam'), ('H?? N???i', 'H?? N???i'), ('H?? T??nh', 'H?? T??nh'), ('H???i D????ng', 'H???i D????ng'), ('H???i Ph??ng', 'H???i Ph??ng'), ('H???u Giang', 'H???u Giang'), ('H??a B??nh', 'H??a B??nh'), ('H??? Ch?? Minh', 'Th??nh ph??? H??? Ch?? Minh'), ('H??ng Y??n', 'H??ng Y??n'), ('Kh??nh Ho??', 'Kh??nh Ho??'), ('Ki??n Giang', 'Ki??n Giang'), ('Kon Tum', 'Kon Tum'), ('Lai Ch??u', 'Lai Ch??u'), ('L???ng S??n', 'L???ng S??n'), ('L??o Cai', 'L??o Cai'), ('L??m ?????ng', 'L??m ?????ng'), ('Long An', 'Long An'), ('Nam ?????nh', 'Nam ?????nh'), ('Ngh??? An', 'Ngh??? An'), ('Ninh B??nh', 'Ninh B??nh'), ('Ninh Thu???n', 'Ninh Thu???n'), ('Ph?? Th???', 'Ph?? Th???'), ('Ph?? Y??n', 'Ph?? Y??n'), ('Qu???ng B??nh', 'Qu???ng B??nh'), ('Qu???ng Nam', 'Qu???ng Nam'), ('Qu???ng Ng??i', 'Qu???ng Ng??i'), ('Qu???ng Ninh', 'Qu???ng Ninh'), ('Qu???ng Tr???', 'Qu???ng Tr???'), ('S??c Tr??ng', 'S??c Tr??ng'), ('S??n La', 'S??n La'), ('T??y Ninh', 'T??y Ninh'), ('Th??i B??nh', 'Th??i B??nh'), ('Th??i Nguy??n', 'Th??i Nguy??n'), ('Thanh H??a', 'Thanh H??a'), ('Th???a Thi??n-Hu???', 'Th???a Thi??n-Hu???'), ('Ti???n Giang', 'Ti???n Giang'), ('Tr?? Vinh', 'Tr?? Vinh'), ('Tuy??n Quang', 'Tuy??n Quang'), ('V??nh Long', 'V??nh Long'), ('V??nh Ph??c', 'V??nh Ph??c'), ('Y??n B??i', 'Y??n B??i')], default='H??? Ch?? Minh', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
