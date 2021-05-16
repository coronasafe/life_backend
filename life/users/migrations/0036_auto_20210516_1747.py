# Generated by Django 2.2.11 on 2021-05-16 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_auto_20210516_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, default=2, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Non-binary')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')]),
        ),
    ]
