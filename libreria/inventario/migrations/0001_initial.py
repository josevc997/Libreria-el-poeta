# Generated by Django 4.0.4 on 2022-05-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30, null=True)),
                ('rut', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30, null=True)),
                ('correo', models.CharField(max_length=30, null=True)),
                ('telefono', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
    ]
