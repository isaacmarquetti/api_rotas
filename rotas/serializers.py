from rest_framework import serializers
from rotas import models


class LocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Local
        fields = '__all__'


class RotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rota
        fields = ['source', 'target', 'distance']
