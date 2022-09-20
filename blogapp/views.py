from django.shortcuts import render
from blogapp.models import Post, Categoria

# Create your views here.

def blog(request):
    var_post=Post.objects.all()
    return render(request, "Tblogs/blog.html", {"posts":var_post})

def categoria(request, categoria_id):
    var_categoria=Categoria.objects.get(id=categoria_id)
    var_post=Post.objects.filter(categorias=var_categoria)
    return render(request, "Tblogs/categorias.html", {"categoria":var_categoria, "posts":var_post})

