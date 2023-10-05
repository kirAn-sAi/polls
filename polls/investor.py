from django.db import models


class Investor(models.Model):
    name = models.CharField(max_length=500, verbose_name="Investor Name")
    created_by = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images', verbose_name="Logo", null=True)
    twitter_handle = models.CharField(verbose_name="Twitter Handle", null=True)
    delete_info = models.CharField(max_length=100, null=True)
    mapped_inv_id = models.IntegerField(null=True)
    site_link = models.CharField(verbose_name="Site Link",null=True)

    def __str__(self):
        return f"{self.name}"
