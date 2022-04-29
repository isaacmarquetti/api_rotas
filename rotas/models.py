from django.db import models


class Rota(models.Model):
    source = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    distance = models.IntegerField()
