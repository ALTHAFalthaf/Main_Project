# Generated by Django 4.2.5 on 2023-11-26 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_customuser_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Immunogen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('definition', models.CharField(blank=True, max_length=100, null=True)),
                ('disease_handled', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_immunized', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('exp_date', models.DateTimeField(blank=True, null=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='vaccine.record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.CharField(choices=[('B', 'Birth'), ('6w', '6 weeks (Infants)'), ('10w', '10 weeks (Infants)'), ('14w', '14 weeks (Infants)'), ('6m', '6 moonths (Infants)'), ('9m', '9 months (Infants)'), ('12m', '12-24 months (Infants)'), ('15m', '15-18 months (Infants)'), ('24m', '24 months (Infants)'), ('L', 'Less than 13 years ')], max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('imu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imus', to='vaccine.immunogen')),
            ],
        ),
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=30)),
                ('schedule_done', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules_done', to='vaccine.schedule')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='vaccine_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccines', to='vaccine.vaccine'),
        ),
        migrations.CreateModel(
            name='RecordView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
