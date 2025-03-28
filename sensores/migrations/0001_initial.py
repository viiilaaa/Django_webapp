# Generated by Django 5.0.4 on 2025-03-26 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identificador', models.CharField(max_length=100, unique=True)),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('fecha_instalacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('mantenimiento', 'En Mantenimiento')], default='activo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MedicionSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_medicion', models.DateTimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediciones', to='sensores.sensor')),
            ],
        ),
    ]
