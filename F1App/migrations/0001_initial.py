# Generated by Django 4.2.8 on 2024-01-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.PositiveIntegerField()),
                ('vuelta_rapida', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('equipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Puntos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.PositiveIntegerField()),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F1App.carrera')),
            ],
        ),
        migrations.AddField(
            model_name='carrera',
            name='piloto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F1App.piloto'),
        ),
    ]