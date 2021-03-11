from django.db import models
from django.contrib.auth.models import User

class UserWhiskey(models.Model):

    title = models.CharField(max_length=50)
    list_image_url = models.CharField(max_length=255)
    notes = models.CharField(max_length=500)
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    whiskey = models.ForeignKey("Whiskey", on_delete=models.CASCADE)