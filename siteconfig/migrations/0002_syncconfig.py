# Generated by Django 4.1.5 on 2023-02-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteconfig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('isEnable', models.BooleanField(default=True)),
            ],
        ),
    ]
