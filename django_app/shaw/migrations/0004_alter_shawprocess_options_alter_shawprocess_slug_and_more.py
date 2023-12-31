# Generated by Django 4.1.7 on 2023-09-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaw', '0003_alter_shawprocess_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shawprocess',
            options={'ordering': ['-created_at'], 'verbose_name': 'shaw_process', 'verbose_name_plural': 'shaw_processes'},
        ),
        migrations.AlterField(
            model_name='shawprocess',
            name='slug',
            field=models.SlugField(default='f27d2939-7e94-4706-b6f2-8f2d467066cd', max_length=100, unique=True),
        ),
        migrations.AddConstraint(
            model_name='shawprocess',
            constraint=models.UniqueConstraint(fields=('formation_area', 'sub_formation_area', 'formation_environment', 'title'), name='unique_shaw_title_per_formation_environment'),
        ),
    ]
