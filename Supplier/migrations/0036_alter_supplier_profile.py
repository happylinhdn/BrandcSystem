# Generated by Django 4.1.5 on 2023-02-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0035_alter_supplier_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='profile',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='PROFILE/QUOTATION'),
        ),
    ]
