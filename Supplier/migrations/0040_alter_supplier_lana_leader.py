# Generated by Django 4.1.5 on 2023-02-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0039_alter_supplier_booking_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='lana_leader',
            field=models.BooleanField(),
        ),
    ]
