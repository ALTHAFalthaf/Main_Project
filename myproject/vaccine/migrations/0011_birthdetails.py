# Generated by Django 3.2 on 2024-02-18 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0010_auto_20240218_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_birth', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('regno', models.CharField(max_length=50)),
                ('rchid', models.CharField(max_length=50)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
