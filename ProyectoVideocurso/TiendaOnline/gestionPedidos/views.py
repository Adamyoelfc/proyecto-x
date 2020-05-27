from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulo

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje = "articulo buscado: %r" %request.GET["prd"]

        producto = request.GET["prd"]

        articulos = Articulo.objects.filter(nombre_icontains = producto)

        return render(request, "resultados_busquedas.html", {"articulos" : articulos, "query" : producto})

    else:
        mensaje = "no has introducido nada"

    return HttpResponse(mensaje)