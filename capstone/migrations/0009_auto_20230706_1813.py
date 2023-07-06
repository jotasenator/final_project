# Generated by Django 4.2.2 on 2023-07-06 17:18

from django.db import migrations


def create_footer(apps, schema_editor):
    Footer = apps.get_model("capstone", "Footer")
    Footer.objects.create(
        company_name="Your Company Name",
        company_address="Your Company Address",
        company_phone="Your Company Phone",
        company_email="Your Company Email",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("capstone", "0008_footer"),
    ]

    operations = [migrations.RunPython(create_footer)]
