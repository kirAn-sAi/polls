from django.db import models
from . import constants
from .location import Location
from .organization import Organization


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    start_date = models.DateField()
    end_date = models.DateField()
    allocated_budget = models.FloatField()
    team_size = models.IntegerField(default=3)
    is_deployed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT, null=True)
    org = models.ForeignKey(Organization, on_delete=models.RESTRICT, null=True)
    stage = models.IntegerField(
        default=constants.DRAFT,
        choices=constants.PROJECT_STATUS,
    )

    def __str__(self):
        return self.name
