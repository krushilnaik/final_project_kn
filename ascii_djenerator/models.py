"""
Models
"""

from django.db import models

# Create your models here.


class Letter(models.Model):
    """
    Representation of each character that makes up an "art".
    "|"-separated for easy splitting and interweaving
    """

    letter = models.CharField(max_length=1)
    representation = models.CharField(max_length=49)
