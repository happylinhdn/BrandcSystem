# Generated by Django 4.1.5 on 2023-02-01 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0026_alter_supplier_engagement_rate_absolute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='location',
            field=models.CharField(choices=[('AG', 'An Giang'), ('BV', 'Bà Rịa-Vũng Tàu'), ('BL', 'Bạc Liêu'), ('BK', 'Bắc Kạn'), ('BG', 'Bắc Giang'), ('BN', 'Bắc Ninh'), ('BT', 'Bến Tre'), ('BD', 'Bình Dương'), ('BĐ', 'Bình Định'), ('BP', 'Bình Phước'), ('BTH', 'Bình Thuận'), ('CM', 'Cà Mau'), ('CB', 'Cao Bằng'), ('CT', 'Cần Thơ'), ('ĐNA', 'Đà Nẵng'), ('ĐL', 'Đắk Lắk'), ('ĐNO', 'Đắk Nông'), ('ĐB', 'Điện Biên'), ('ĐN', 'Đồng Nai'), ('ĐT', 'Đồng Tháp'), ('GL', 'Gia Lai'), ('HG', 'Hà Giang'), ('HNA', 'Hà Nam'), ('HN', 'Hà Nội'), ('HT', 'Hà Tĩnh'), ('HD', 'Hải Dương'), ('HP', 'Hải Phòng'), ('HGI', 'Hậu Giang'), ('HB', 'Hòa Bình'), ('SG', 'Thành phố Hồ Chí Minh'), ('HY', 'Hưng Yên'), ('KH', 'Khánh Hoà'), ('KG', 'Kiên Giang'), ('KT', 'Kon Tum'), ('LC', 'Lai Châu'), ('LS', 'Lạng Sơn'), ('LCA', 'Lào Cai'), ('LĐ', 'Lâm Đồng'), ('LA', 'Long An'), ('NĐ', 'Nam Định'), ('NA', 'Nghệ An'), ('NB', 'Ninh Bình'), ('NT', 'Ninh Thuận'), ('PT', 'Phú Thọ'), ('PY', 'Phú Yên'), ('QB', 'Quảng Bình'), ('QNA', 'Quảng Nam'), ('QNG', 'Quảng Ngãi'), ('QN', 'Quảng Ninh'), ('QT', 'Quảng Trị'), ('ST', 'Sóc Trăng'), ('SL', 'Sơn La'), ('TN', 'Tây Ninh'), ('TB', 'Thái Bình'), ('TNG', 'Thái Nguyên'), ('TH', 'Thanh Hóa'), ('TTH', 'Thừa Thiên-Huế'), ('TG', 'Tiền Giang'), ('TV', 'Trà Vinh'), ('TQ', 'Tuyên Quang'), ('VL', 'Vĩnh Long'), ('VP', 'Vĩnh Phúc'), ('YB', 'Yên Bái')], default='SG', max_length=3),
        ),
    ]
