# Generated by Django 4.1.7 on 2023-09-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaw', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shawprocess',
            name='slug',
            field=models.SlugField(default='5f6948ed-01ea-4a0e-a2da-f20d8cce1fc8', max_length=100, unique=True),
        ),
    ]
