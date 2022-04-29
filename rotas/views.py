from django.http import HttpResponse

from rest_framework import viewsets

from .models import Rota
from rotas.api.serializers import RotaSerializer


def home(request):
    return HttpResponse('Olá Mundo!')


class RotaAPIViewSet(viewsets.ModelViewSet):
    serializer_class = RotaSerializer
    queryset = Rota.objects.all()