from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    buildings_count = models.IntegerField(default=1)
    seating_capacity = models.IntegerField(null=True)
    parking_capacity = models.IntegerField(null=True)
    cafeteria_capacity = models.IntegerField(null=True)

    def __str__(self):
        return self.name

