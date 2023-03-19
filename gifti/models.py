from django.db import models
from django.contrib.auth.models import User



class BrandName(models.Model):
    brand_name = models.CharField(max_length=100)


class StoreName(models.Model):
    store_name = models.CharField(max_length=100)


class Wish(models.Model):
    item = models.CharField(max_length=200) 
    brand = models.ForeignKey(BrandName, related_name="wish", on_delete=models.PROTECT)
    picture = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    store = models.ManyToManyField(StoreName, related_name="wish")
    color = models.CharField(max_length=100, null=True, blank=True)
    style = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(max_length=100, null=True, blank=True)
    bought = models.BooleanField()
    nametag = models.ForeignKey(User, related_name="nametag", on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.brand + self.item

