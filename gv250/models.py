from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


# Create your models here.
class Member(AbstractUser):
    BASKAN = "BASKAN"
    KOORDINATOR = "KOORDINATOR"
    DISIPLIN = "DISIPLIN"
    KOC = "KOC"
    SAYMAN = "SAYMAN"
    UYE = "UYE"
    CIRAK = "CIRAK"
    CAYLAK = "CAYLAK"
    POSITIONS = [
        (BASKAN, "BASKAN"),
        (KOORDINATOR, "KOORDINATOR"),
        (DISIPLIN, "DISIPLIN"),
        (KOC, "KOC"),
        (SAYMAN, "SAYMAN"),
        (UYE, "UYE"),
        (CIRAK, "CIRAK"),
        (CAYLAK, "CAYLAK"),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tc_no = models.CharField(max_length=200)
    license_no = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    birthday = models.DateTimeField()
    position = models.CharField(choices=POSITIONS, default=CAYLAK, max_length=100)
    blood_type = models.CharField(max_length=30)
    application_date = models.DateTimeField(auto_now_add=True)
    club_entry_date = models.DateTimeField(blank=True, null=True)
    job = models.CharField(max_length=200)
    date_of_oath = models.DateTimeField(blank=True, null=True)
    motorcycle_model = models.CharField(max_length=150)
    engine_capacity = models.IntegerField()
    license_plate = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    emergency_tel = models.CharField(max_length=50)
    vest_freeze = models.DateTimeField(blank=True, null=True)

