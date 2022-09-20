from dataclasses import fields
from email import message
from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

'''def autenticacion(request):
    return  render(request, "Tregistro/registro.html")'''

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    
class Vregistro(View):
    
    
    def get(self, request):
        #form=UserCreationForm()
        return render(request, "Tregistro/registro.html", {'form':RegistroUserForm()})
    
    def post(self, request):
        #form=UserCreationForm(request.POST)
        form=RegistroUserForm(request.POST)    
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
        return render(request, "Tregistro/registro.html", {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method=="POST": #si se pulsa el boton de login
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            passwo=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=passwo)
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")
                  
    var_form=AuthenticationForm()
    return render(request, "Tlogin/login.html", {"form":var_form})
    
    
        
