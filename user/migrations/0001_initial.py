# Generated by Django 4.0.4 on 2022-04-19 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zones', models.PositiveSmallIntegerField(choices=[(1, 'West'), (2, 'East')], default=1, verbose_name='Sector')),
            ],
            options={
                'verbose_name_plural': 'Sector',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, verbose_name='Name of the location')),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='still active?')),
                ('address', models.CharField(max_length=125, verbose_name='Address of the location')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.sector')),
            ],
            options={
                'verbose_name_plural': 'Locations available',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('isDoctor', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ssn', models.IntegerField(unique=True, verbose_name='Social security number')),
                ('home_address', models.CharField(max_length=65, verbose_name='Home address')),
                ('phone_num', models.CharField(max_length=15, verbose_name='Phone number')),
                ('specialty', models.CharField(max_length=65, verbose_name='Specialty fo the doctor')),
                ('office_address', models.CharField(max_length=150, verbose_name='Office address')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.sector')),
                ('zones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.location')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
    ]
