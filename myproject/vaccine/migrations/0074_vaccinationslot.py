# Generated by Django 4.2.5 on 2024-03-30 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0073_remove_vaccinationslot_child_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine', models.CharField(choices=[('BCG', 'BCG'), ('OPV', 'OPV'), ('HEB B', 'HEB B'), ('DPT', 'DPT'), ('IPV', 'IPV'), ('MEASLES', 'Measles'), ('VITAMIN A', 'Vitamin A'), ('JE', 'JE'), ('OPV BOOSTER', 'OPV Booster'), ('DDT BOOSTER', 'DDT Booster'), ('DPT BOOSTER', 'DPT Booster'), ('TT', 'TT(Tetanus Toxoid)')], max_length=20)),
                ('booking_date', models.DateField()),
                ('slot', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=20)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.birthdetails')),
            ],
        ),
    ]
