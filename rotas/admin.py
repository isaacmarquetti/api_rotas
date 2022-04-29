from django.contrib import admin

from .models import Rota


@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ('source', 'target', 'distance')
