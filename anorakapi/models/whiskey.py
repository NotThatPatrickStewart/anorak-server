from django.db import models

class Whiskey(models.Model):

    title = models.CharField(max_length=50)
    list_img_url = models.CharField(max_length=255)
    region = models.CharField(max_length=50)
    price = models.FloatField()

    