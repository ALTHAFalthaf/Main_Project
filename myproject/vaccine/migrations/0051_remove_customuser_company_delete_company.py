# Generated by Django 4.2.5 on 2024-03-06 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0050_vaccine_vaccinepurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
