from django.shortcuts import render
from tiendaapp.models import Producto

# Create your views here.


def tienda(request):
    var_productos=Producto.objects.all()
    return render(request, "Ttiendas/tienda.html", {"productos":var_productos})



