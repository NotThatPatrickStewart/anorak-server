from django.db import models

class Whiskey(models.Model):

    title = models.CharField(max_length=50)
    comparable = models.CharField(max_length=50)
    list_image_url = models.CharField(max_length=255)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    region = models.CharField(max_length=50)
    price = models.FloatField()