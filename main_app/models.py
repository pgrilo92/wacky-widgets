from django.db import models

class WackyWidget(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
