from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.prosesar_pedido, name="Pedidos"),
   
]

