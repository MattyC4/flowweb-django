from django.urls import path
from .views import index_view, usuarios_view, medidores_view, consumos_view, boletas_view, reportes_view

app_name = "dashboard"

urlpatterns = [
    path("", index_view, name="index"),
    path("usuarios/", usuarios_view, name="usuarios"),
    path("medidores/", medidores_view, name="medidores"),
    path("consumos/", consumos_view, name="consumos"),
    path("boletas/", boletas_view, name="boletas"),
    path("reportes/", reportes_view, name="reportes"),
]
