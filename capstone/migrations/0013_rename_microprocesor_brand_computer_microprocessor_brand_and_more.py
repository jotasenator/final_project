# Generated by Django 4.2.2 on 2023-07-08 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0012_remove_computer_user_computer_responsible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='microprocesor_brand',
            new_name='microprocessor_brand',
        ),
        migrations.RenameField(
            model_name='computer',
            old_name='microprocesor_memory_model',
            new_name='microprocessor_model',
        ),
        migrations.RenameField(
            model_name='computer',
            old_name='microprocesor_serial_number',
            new_name='microprocessor_serial_number',
        ),
    ]
