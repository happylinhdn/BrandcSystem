# Generated by Django 4.1.5 on 2023-02-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0040_alter_supplier_lana_leader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='lana_leader',
            field=models.BooleanField(default=True),
        ),
    ]