from django.db import models


class Local(models.Model):
    """
    Método para atribuir um local como exemplo.
    """
    local = models.CharField(max_length=30)

    def __str__(self):
        return self.local

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'


class Rota(models.Model):
    """
    Método para criar rotas entre os locais criados como exemplo.

    Ao definir um local de origem "source" e um ponto de chegada "target",
    é atribuido uma distância entre dois pontos em uma rota unidirecional.
    """
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

    class Meta:
        verbose_name = 'Rota'
        verbose_name_plural = 'Rotas'
