from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse

# Create your models here.
class Rank(models.Model):
    name = models.CharField(max_length=31)
    slug = AutoSlugField(populate_from="name", unique=True)
    score = models.IntegerField()

    class Meta:
        ordering =["-score"]

    def __str__(self):
        return self.name