# Generated by Django 4.2.2 on 2023-07-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0009_auto_20230706_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intranet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_intranet', models.CharField(max_length=255)),
            ],
        ),
    ]
