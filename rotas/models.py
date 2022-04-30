from django.db import models


class Local(models.Model):
    local = models.CharField(max_length=30)

    def __str__(self):
        return self.local


class Rota(models.Model):
    Town = (
        ('A', 'Exemplo A'),
        ('B', 'Exemplo B'),
        ('C', 'Exemplo C'),
        ('D', 'Exemplo D'),
        ('E', 'Exemplo E'),
    )
    source = models.CharField(max_length=1, choices=Town, blank=False, null=False)
    target = models.CharField(max_length=1, choices=Town, blank=False, null=False)
    distance = models.IntegerField()

    def __str__(self):
        return self.source

