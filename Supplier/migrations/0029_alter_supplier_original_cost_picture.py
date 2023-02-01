# Generated by Django 4.1.5 on 2023-02-01 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0028_alter_supplier_original_cost_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='original_cost_picture',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True, verbose_name='ORIGINAL COST - PICTURE'),
        ),
    ]
