from django.db import models
from django.conf import settings

class Records(models.Model):
    artist = models.CharField("artist", max_length=128)
    title = models.CharField("title", max_length=128)
    price = models.IntegerField("price")
    country = models.CharField("country", max_length=128)
    released = models.CharField("released", max_length=128)
    genre = models.CharField("genre", max_length=128)
    
    def __str__(self):
        return self.title