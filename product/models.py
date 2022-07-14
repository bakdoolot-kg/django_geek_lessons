from django.db import models


class Vegetables(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)