from django.http import HttpResponse

from rest_framework import viewsets

from .models import Rota, Local
from rotas.serializers import RotaSerializer, LocalSerializer


def home(request):
    return HttpResponse('Olá Mundo!')


class LocalAPIViewSet(viewsets.ModelViewSet):
    serializer_class = LocalSerializer
    queryset = Local.objects.all()


class RotaAPIViewSet(viewsets.ModelViewSet):
    serializer_class = RotaSerializer
    queryset = Rota.objects.all()