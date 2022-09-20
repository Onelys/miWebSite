from django.shortcuts import render, redirect
from .forms import ContactoForms
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
    
    formulario_contacto=ContactoForms()
    
    if request.method=="POST":
        formulario_contacto=ContactoForms(data=request.POST)
        if formulario_contacto.is_valid():
            var_nombre=request.POST.get("nombre")
            var_email=request.POST.get("email")
            var_contenido=request.POST.get("contenido")
            
            var_email=EmailMessage("Mensaje desde App Django", 
                                   "El usuario : {}. Con la direccion : {}. Escribe lo siguiente : {}."
                                   .format(var_nombre,var_email,var_contenido),
                                   "",["jairoonelys@gmail.com"], reply_to=[var_email])
            try:
                var_email.send()
                
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")
        
    return render(request, "Tcontactos/contacto.html", {'miFormulario':formulario_contacto})