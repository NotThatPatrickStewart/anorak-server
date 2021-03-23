from django.db import models

class WhiskeyTag(models.Model):

    whiskey = models.ForeignKey("Whiskey", on_delete=models.CASCADE, related_name="relatedwhiskey")
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, related_name="relatedtag")
    count = models.IntegerField()
    normalized_count = models.IntegerField()
