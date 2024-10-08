# Generated by Django 4.2.16 on 2024-09-17 23:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Car Make')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Car Model')),
                ('type', models.CharField(choices=[('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon')], default='SUV', max_length=10, verbose_name='Type of Car')),
                ('year', models.IntegerField(default=2023, validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(2015)], verbose_name='Manufacture Year')),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake', verbose_name='Car Make')),
            ],
        ),
    ]
