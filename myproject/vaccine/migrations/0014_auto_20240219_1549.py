# Generated by Django 3.2 on 2024-02-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0013_birthdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthdetails',
            name='height',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='birthdetails',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='birthdetails',
            name='rchid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='birthdetails',
            name='regno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='birthdetails',
            name='weight',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
    ]
