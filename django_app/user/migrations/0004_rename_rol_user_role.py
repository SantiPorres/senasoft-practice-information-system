# Generated by Django 4.1.7 on 2023-09-23 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_rol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='rol',
            new_name='role',
        ),
    ]
