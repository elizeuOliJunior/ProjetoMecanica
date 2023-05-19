from django.urls import path
from . import views

#verifica se o caminho existe
urlpatterns = [
    path('' , views.clientes, name="clientes" )
]