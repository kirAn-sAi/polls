from django.db import models
from django.contrib.postgres.fields import ArrayField


class Organization(models.Model):
    name = models.CharField(max_length=50)
    base_country = models.CharField(max_length=25)
    office_locations = models.IntegerField(default=1)
    domain = models.CharField(max_length=50)
    projects = ArrayField(models.CharField(max_length=255), null=True)

    def __str__(self):
        return f"{self.name} - {self.base_country}"
