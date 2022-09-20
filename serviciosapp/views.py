from django.shortcuts import render
from serviciosapp.models import Servicio

# Create your views here.

def servicios(request):
    var_servicios=Servicio.objects.all()
    return render(request, "Tservicios/servicios.html", {"servicios":var_servicios})
