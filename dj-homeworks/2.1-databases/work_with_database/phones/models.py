from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.CharField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
