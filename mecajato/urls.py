from django.contrib import admin
from django.urls import path , include

#verifica se /clientes existe
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/' , include ('clientes.urls')) #inclui um novo arquivo
]
