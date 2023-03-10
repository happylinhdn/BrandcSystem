# Generated by Django 4.1.5 on 2023-01-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0023_supplier_kol_tier_alter_supplier_follower_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='engagement_rate_absolute',
            field=models.FloatField(blank=True, editable=False, max_length=20, null=True, verbose_name='ER (Ab.)'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='engagement_rate_absolute_display',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True, verbose_name='ER (Ab.)'),
        ),
    ]
