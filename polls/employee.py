from django.db import models
from . import constants
from .organization import Organization


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=1,
        choices=constants.GENDER_CHOICES,
        default=constants.MALE,
    )
    nationality = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)
    skills = models.CharField(max_length=500)
    org = models.ForeignKey(Organization, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
