from django.shortcuts import render, HttpResponse

from carritoapp.carrito import Carrito


# Create your views here.

def home(request):
    #carrito=Carrito(request)--->otra manera de hacerlo para que no de error al inicio
    return render(request, "miWebSiteapp/home.html")#(lee archivo html)
    #return HttpResponse("Inicio") ----paraprobar al inicio de que esta funcionando (lee texto)



'''def tienda(request):
    return render(request, "miWebSiteapp/tienda.html")'''



