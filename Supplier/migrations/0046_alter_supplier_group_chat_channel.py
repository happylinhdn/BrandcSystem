# Generated by Django 4.1.5 on 2023-02-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0045_alter_supplier_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='group_chat_channel',
            field=models.CharField(choices=[('Zalo', 'Zalo'), ('Viber', 'Viber'), ('Facebook', 'Facebook')], default='Zalo', max_length=8, null=True, verbose_name='Group Chat Channel'),
        ),
    ]
