# Generated by Django 4.2.2 on 2023-07-05 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0005_profile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]
