from django.db import models


class Event(models.Model):
    evt_image = models.ImageField(upload_to='event_images/')
    evt_short_description = models.CharField(max_length=300)
