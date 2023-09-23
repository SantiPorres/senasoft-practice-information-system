# Generated by Django 4.1.7 on 2023-09-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environmental', '0003_alter_environmentalprocess_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='environmentalprocess',
            options={'ordering': ['-created_at'], 'verbose_name': 'environmental_process', 'verbose_name_plural': 'environmental_processes'},
        ),
        migrations.AlterField(
            model_name='environmentalprocess',
            name='slug',
            field=models.SlugField(default='28faf19f-2ed0-4ec2-a45f-a0c3b4803b7d', max_length=100, unique=True),
        ),
        migrations.AddConstraint(
            model_name='environmentalprocess',
            constraint=models.UniqueConstraint(fields=('formation_area', 'sub_formation_area', 'formation_environment', 'title'), name='unique_title_per_formation_environment'),
        ),
    ]