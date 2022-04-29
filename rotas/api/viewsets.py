from rest_framework import viewsets
from rotas import models
from rotas.api import serializers


class RotasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RotaSerializer
    queryset = models.Rota.objects.all()
