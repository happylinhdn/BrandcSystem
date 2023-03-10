# Generated by Django 4.1.5 on 2023-03-01 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0072_alter_supplier_kpi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='booking_contact_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='booking_contact_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='booking_contact_phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='channel',
            field=models.CharField(choices=[('Facebook Group', 'Facebook Group'), ('Facebook Fanpage', 'Facebook Fanpage'), ('Facebook Personal', 'Facebook Personal'), ('Tiktok Community', 'Tiktok Community'), ('Tiktok Personal', 'Tiktok Personal'), ('Youtube Community', 'Youtube Community'), ('Youtube Personal', 'Youtube Personal'), ('Instagram', 'Instagram'), ('Forum', 'Forum'), ('Website', 'Website'), ('Linkedin', 'Linkedin'), ('Others', 'Others')], max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='discount',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='engagement_rate_absolute',
            field=models.FloatField(editable=False, null=True, verbose_name='ER (Ab.)'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='engagement_rate_percent',
            field=models.FloatField(null=True, verbose_name='ER(%)'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='group_chat_channel',
            field=models.CharField(choices=[('Zalo', 'Zalo'), ('Viber', 'Viber'), ('Facebook', 'Facebook')], max_length=8, null=True, verbose_name='Group Chat Channel'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='group_chat_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='handle_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='kol_tier',
            field=models.CharField(editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='kpi',
            field=models.CharField(max_length=50, null=True, verbose_name='KPI'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='lana_leader',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='latest_update',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='original_cost_event',
            field=models.DecimalField(decimal_places=0, max_digits=20, null=True, verbose_name='Org. cost - Event'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='original_cost_picture',
            field=models.DecimalField(decimal_places=0, max_digits=20, null=True, verbose_name='Org. cost - Picture'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='original_cost_tvc',
            field=models.DecimalField(decimal_places=0, max_digits=20, null=True, verbose_name='Org. cost - TVC'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='original_cost_video',
            field=models.DecimalField(decimal_places=0, max_digits=20, null=True, verbose_name='Org. cost - Video'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='profile',
            field=models.CharField(max_length=300, null=True, verbose_name='Profile/Quotation'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
