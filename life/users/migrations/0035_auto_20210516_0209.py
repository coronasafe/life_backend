# Generated by Django 2.2.11 on 2021-05-15 20:39

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_auto_20201122_2013'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
