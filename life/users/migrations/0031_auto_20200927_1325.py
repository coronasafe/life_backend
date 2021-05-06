# Generated by Django 2.2.11 on 2020-09-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20200921_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(2, 'Transaportation'), (3, 'Pharmacist'), (5, 'Volunteer'), (9, 'StaffReadOnly'), (10, 'Staff'), (15, 'Doctor'), (20, 'Reserved'), (21, 'WardAdmin'), (23, 'LocalBodyAdmin'), (25, 'DistrictLabAdmin'), (29, 'DistrictReadOnlyAdmin'), (30, 'DistrictAdmin'), (35, 'StateLabAdmin'), (39, 'StateReadOnlyAdmin'), (40, 'StateAdmin')]),
        ),
    ]
