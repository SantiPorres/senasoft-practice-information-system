# Generated by Django 4.1.7 on 2023-09-13 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environmental', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formation_area', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='environmentalprocess',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='environmental_processes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='environmentalprocess',
            name='formation_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='environmental_processes', to='formation_area.formationarea'),
        ),
        migrations.AddField(
            model_name='environmentalprocess',
            name='formation_environment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='environmental_processes', to='formation_area.formationenvironment'),
        ),
        migrations.AddField(
            model_name='environmentalprocess',
            name='sub_formation_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='environmental_processes', to='formation_area.subformationarea'),
        ),
    ]
