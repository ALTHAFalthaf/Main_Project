# Generated by Django 3.2 on 2024-03-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0044_vaccine_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
