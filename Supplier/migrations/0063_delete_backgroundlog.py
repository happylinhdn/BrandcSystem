# Generated by Django 4.1.5 on 2023-02-15 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0062_alter_backgroundlog_log'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BackgroundLog',
        ),
    ]
