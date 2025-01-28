from django.urls import path

from . import views

urlpatterns = [
    path('', views.relatorioViews, name="relatorios-index"),
]