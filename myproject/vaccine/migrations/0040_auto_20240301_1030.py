# Generated by Django 3.2 on 2024-03-01 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0039_vaccine_vaccinepurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinepurchase',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='vaccinepurchase',
            name='vaccine',
        ),
        migrations.DeleteModel(
            name='Vaccine',
        ),
        migrations.DeleteModel(
            name='VaccinePurchase',
        ),
    ]