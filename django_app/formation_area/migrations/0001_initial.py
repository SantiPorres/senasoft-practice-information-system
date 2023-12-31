# Generated by Django 4.1.7 on 2023-09-13 04:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormationArea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(default='3939af1e-4025-46cb-aa10-1d3b9eaf2df6', max_length=100, unique=True)),
                ('status', models.CharField(choices=[('AT', 'Active'), ('IN', 'Inactive')], default='AT', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='7e1cb28f-4e4b-44a7-99fb-8d4f95be8b67', max_length=36, unique=True)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'formation_area',
                'verbose_name_plural': 'formation_areas',
                'db_table': 'formation_area',
            },
        ),
        migrations.CreateModel(
            name='SubFormationArea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(default='3939af1e-4025-46cb-aa10-1d3b9eaf2df6', max_length=100, unique=True)),
                ('status', models.CharField(choices=[('AT', 'Active'), ('IN', 'Inactive')], default='AT', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='ca8b95bf-f7b6-4497-9543-40a9c030b301', max_length=36, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('formation_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_formation_areas', to='formation_area.formationarea')),
            ],
            options={
                'verbose_name': 'sub_formation_area',
                'verbose_name_plural': 'sub_formation_areas',
                'db_table': 'sub_formation_area',
            },
        ),
        migrations.CreateModel(
            name='FormationEnvironment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(default='3939af1e-4025-46cb-aa10-1d3b9eaf2df6', max_length=100, unique=True)),
                ('status', models.CharField(choices=[('AT', 'Active'), ('IN', 'Inactive')], default='AT', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='b1835233-6a53-4988-92bb-df21e2088c64', max_length=36, unique=True)),
                ('capacity', models.PositiveSmallIntegerField(default=5)),
                ('formation_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formation_environments', to='formation_area.formationarea')),
                ('sub_formation_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formation_environments', to='formation_area.subformationarea')),
            ],
            options={
                'verbose_name': 'formation_environment',
                'verbose_name_plural': 'formation_environments',
                'db_table': 'formation_environment',
            },
        ),
    ]
