# Generated by Django 2.2.11 on 2021-05-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifedata',
            name='verifiedAndAvailable',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lifedata',
            name='verifiedAndUnavailable',
            field=models.IntegerField(default=0),
        ),
    ]
