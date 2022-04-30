from django.contrib import admin
from .models import Rota, Local


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('id', 'local')


@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ('source', 'target', 'distance')
    list_display_links = ('source', 'target', 'distance')
