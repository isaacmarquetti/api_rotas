from rest_framework import serializers
from rotas import models


class RotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rota
        fields = '__all__'
