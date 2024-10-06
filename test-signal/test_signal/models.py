from django.db import models

CHOICES = [('pass', 'pass'),
           ('fail', 'fail')]


# Create your models here.
class TestCase(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=100, choices=CHOICES)
    epoch = models.IntegerField()
