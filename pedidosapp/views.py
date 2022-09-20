from urllib import request
from webbrowser import get
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carritoapp.carrito import Carrito
from carritoapp.views import limpiar_carrito
from pedidosapp.models import LineaPedido, Pedidos
from django.template.loader import render_to_string
from django.utils.html import strip_tags 
from django.core.mail import send_mail


# Create your views here.

@login_required(login_url="/autenticacion/logear")
def prosesar_pedido(request):
    pedido=Pedidos.objects.create(user=request.user)
    carro=Carrito(request)
    lineas_pedido=list()
    for key, value in carro.carrito.items():
        lineas_pedido.append(LineaPedido(
            
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido   
        ))
        
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,  
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, "El Pedido se a creado correctamente")

    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto="Grasias por su compra"
    mensaje=render_to_string("Temails/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreususario":kwargs.get("nombreusuario")
    })
    
    mensaje_texto=strip_tags(mensaje)
    from_email="jairoonelys@gmail.com"
    #to=kwargs.get("emailusuario")
    to="ingelcon1@gmail.com"
    
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)
    