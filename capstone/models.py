from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Issue(models.Model):
    issue = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(default="")
    phone = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10, default="")
    picture = models.ImageField(upload_to="profile_pictures/")


class Footer(models.Model):
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=20)
    company_email = models.EmailField(default="")
    company_avatar = models.ImageField(upload_to="company_logo/")


class Intranet(models.Model):
    company_intranet = models.CharField(max_length=255)


class Computer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    responsible = models.CharField(max_length=255, default="")

    department = models.CharField(max_length=255)

    seal_number = models.CharField(max_length=255, unique=True)
    computer_name = models.CharField(max_length=255)
    inventory_number_pc = models.CharField(max_length=255)

    motherboard_brand = models.CharField(max_length=255)
    motherboard_model = models.CharField(max_length=255)
    motherboard_serial_number = models.CharField(max_length=255, unique=True)

    hard_disk_brand = models.CharField(max_length=255)
    hard_disk_model = models.CharField(max_length=255)
    hard_disk_serial_number = models.CharField(max_length=255, unique=True)

    ram_memory_brand = models.CharField(max_length=255)
    ram_memory_model = models.CharField(max_length=255)
    ram_memory_serial_number = models.CharField(max_length=255, unique=True)

    microprocessor_brand = models.CharField(max_length=255)
    microprocessor_model = models.CharField(max_length=255)
    microprocessor_serial_number = models.CharField(max_length=255, unique=True)

    psu_internal_brand = models.CharField(max_length=255)
    psu_internal_model = models.CharField(max_length=255)
    psu_internal_serial_number = models.CharField(max_length=255, unique=True)

    cd_dvd_reader_brand = models.CharField(max_length=255)
    cd_dvd_reader_model = models.CharField(max_length=255)
    cd_dvd_reader_serial_number = models.CharField(max_length=255, unique=True)

    monitor_brand = models.CharField(max_length=255)
    monitor_model = models.CharField(max_length=255)
    monitor_serial_number = models.CharField(max_length=255, unique=True)
    monitor_inventory_number = models.CharField(max_length=255)

    keyboard_brand = models.CharField(max_length=255)
    keyboard_model = models.CharField(max_length=255)
    keyboard_serial_number = models.CharField(max_length=255, unique=True)
    keyboard_inventory_number = models.CharField(max_length=255)

    mouse_brand = models.CharField(max_length=255)
    mouse_model = models.CharField(max_length=255)
    mouse_serial_number = models.CharField(max_length=255, unique=True)
    mouse_inventory_number = models.CharField(max_length=255)

    speakers_brand = models.CharField(max_length=255)
    speakers_model = models.CharField(max_length=255)
    speakers_serial_number = models.CharField(max_length=255, unique=True)
    speakers_inventory_number = models.CharField(max_length=255)

    printer_brand = models.CharField(max_length=255)
    printer_model = models.CharField(max_length=255)
    printer_serial_number = models.CharField(max_length=255, unique=True)
    printer_inventory_number = models.CharField(max_length=255)

    psu_external_brand = models.CharField(max_length=255)
    psu_external_model = models.CharField(max_length=255)
    psu_external_serial_number = models.CharField(max_length=255, unique=True)
    psu_external_inventory_number = models.CharField(max_length=255)
