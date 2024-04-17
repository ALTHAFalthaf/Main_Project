# Generated by Django 3.2 on 2024-02-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0007_customuser_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthcareprovider',
            name='areas_of_specialization',
        ),
        migrations.RemoveField(
            model_name='healthcareprovider',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='healthcareprovider',
            name='professional_credentials',
        ),
        migrations.AddField(
            model_name='healthcareprovider',
            name='certification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='healthcareprovider',
            name='license_copy',
            field=models.FileField(blank=True, null=True, upload_to='provider/license_copy/'),
        ),
        migrations.AddField(
            model_name='healthcareprovider',
            name='license_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='healthcareprovider',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='provider/photo/'),
        ),
        migrations.AddField(
            model_name='healthcareprovider',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='provider/resume/'),
        ),
    ]
