# Generated by Django 4.2.5 on 2024-03-20 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0060_birthdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BirthDetails',
        ),
    ]
