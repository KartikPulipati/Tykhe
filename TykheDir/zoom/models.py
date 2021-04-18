from django.db import models
from django.contrib.auth.models import User

class ZoomMtg(models.Model):
    title = models.CharField(max_length=100)
    ZoomUrl = models.URLField(blank=True)
    time = models.TimeField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
