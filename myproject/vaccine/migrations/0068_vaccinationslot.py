# Generated by Django 4.2.5 on 2024-03-28 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0067_remove_vaccinationschedule_notification_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('slot_time', models.TimeField()),
                ('vaccine', models.CharField(choices=[('BCG', 'BCG'), ('OPV', 'OPV'), ('HEB B', 'HEB B'), ('DPT', 'DPT'), ('IPV', 'IPV'), ('MEASLES', 'Measles'), ('VITAMIN A', 'Vitamin A'), ('JE', 'JE'), ('OPV BOOSTER', 'OPV Booster'), ('DDT BOOSTER', 'DDT Booster'), ('DPT BOOSTER', 'DPT Booster'), ('TT', 'TT(Tetanus Toxoid)')], max_length=20)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_slots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
