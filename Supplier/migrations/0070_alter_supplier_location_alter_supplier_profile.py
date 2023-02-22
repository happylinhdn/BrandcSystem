# Generated by Django 4.1.5 on 2023-02-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0069_alter_supplier_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='location',
            field=models.CharField(choices=[('Toàn Quốc', 'Toàn Quốc'), ('An Giang', 'An Giang'), ('Bà Rịa-Vũng Tàu', 'Bà Rịa-Vũng Tàu'), ('Bạc Liêu', 'Bạc Liêu'), ('Bắc Kạn', 'Bắc Kạn'), ('Bắc Giang', 'Bắc Giang'), ('Bắc Ninh', 'Bắc Ninh'), ('Bến Tre', 'Bến Tre'), ('Bình Dương', 'Bình Dương'), ('Bình Định', 'Bình Định'), ('Bình Phước', 'Bình Phước'), ('Bình Thuận', 'Bình Thuận'), ('Cà Mau', 'Cà Mau'), ('Cao Bằng', 'Cao Bằng'), ('Cần Thơ', 'Cần Thơ'), ('Đà Nẵng', 'Đà Nẵng'), ('Đắk Lắk', 'Đắk Lắk'), ('Đắk Nông', 'Đắk Nông'), ('Điện Biên', 'Điện Biên'), ('Đồng Nai', 'Đồng Nai'), ('Đồng Tháp', 'Đồng Tháp'), ('Gia Lai', 'Gia Lai'), ('Hà Giang', 'Hà Giang'), ('Hà Nam', 'Hà Nam'), ('Hà Nội', 'Hà Nội'), ('Hà Tĩnh', 'Hà Tĩnh'), ('Hải Dương', 'Hải Dương'), ('Hải Phòng', 'Hải Phòng'), ('Hậu Giang', 'Hậu Giang'), ('Hòa Bình', 'Hòa Bình'), ('Hồ Chí Minh', 'Thành phố Hồ Chí Minh'), ('Hưng Yên', 'Hưng Yên'), ('Khánh Hoà', 'Khánh Hoà'), ('Kiên Giang', 'Kiên Giang'), ('Kon Tum', 'Kon Tum'), ('Lai Châu', 'Lai Châu'), ('Lạng Sơn', 'Lạng Sơn'), ('Lào Cai', 'Lào Cai'), ('Lâm Đồng', 'Lâm Đồng'), ('Đà Lạt', 'Đà Lạt'), ('Long An', 'Long An'), ('Nam Định', 'Nam Định'), ('Nghệ An', 'Nghệ An'), ('Ninh Bình', 'Ninh Bình'), ('Ninh Thuận', 'Ninh Thuận'), ('Phú Thọ', 'Phú Thọ'), ('Phú Yên', 'Phú Yên'), ('Quảng Bình', 'Quảng Bình'), ('Quảng Nam', 'Quảng Nam'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Quảng Ninh', 'Quảng Ninh'), ('Quảng Trị', 'Quảng Trị'), ('Sóc Trăng', 'Sóc Trăng'), ('Sơn La', 'Sơn La'), ('Tây Ninh', 'Tây Ninh'), ('Thái Bình', 'Thái Bình'), ('Thái Nguyên', 'Thái Nguyên'), ('Thanh Hóa', 'Thanh Hóa'), ('Thừa Thiên-Huế', 'Thừa Thiên-Huế'), ('Tiền Giang', 'Tiền Giang'), ('Trà Vinh', 'Trà Vinh'), ('Tuyên Quang', 'Tuyên Quang'), ('Vĩnh Long', 'Vĩnh Long'), ('Vĩnh Phúc', 'Vĩnh Phúc'), ('Yên Bái', 'Yên Bái'), ('Nước Ngoài', 'Nước Ngoài')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='profile',
            field=models.CharField(max_length=300, null=True, verbose_name='Profile/Quotation'),
        ),
    ]
