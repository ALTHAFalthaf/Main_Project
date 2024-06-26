# Generated by Django 3.2 on 2024-02-18 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0009_rename_contact_number_healthcareprovider_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthcareprovider',
            name='address',
        ),
        migrations.RemoveField(
            model_name='healthcareprovider',
            name='city',
        ),
        migrations.RemoveField(
            model_name='healthcareprovider',
            name='country',
        ),
        migrations.RemoveField(
            model_name='healthcareprovider',
            name='state',
        ),
        migrations.AlterField(
            model_name='healthcareprovider',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='healthcareprovider',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='healthcare_provider_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
