
from django.urls import path
from . import views
from .views import Vregistro, cerrar_sesion, logear


urlpatterns = [
   
    #path('', views.autenticacion, name="Autenticacion"),
    path('', Vregistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
    path('logear', logear, name="Logear"),
     
]