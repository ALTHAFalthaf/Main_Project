# Generated by Django 4.2.5 on 2024-03-06 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0052_company_customuser_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
    ]
