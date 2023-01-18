# Generated by Django 4.1.5 on 2023-01-18 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0010_alter_supplier_channel_alter_supplier_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
