from django.shortcuts import render
from django.http import HttpResponse
from AppLuis.models import * 
from django.template import Template, loader
from AppLuis.forms import *


# Create your views here.
def inicio(request):
    return render(request, "AppLuis/inicio.html")

def piloto(request):
    return render(request, "AppLuis/piloto.html")

def scuderia(request):
    return render(request, "AppLuis/scuderia.html")

def circuito(request):
    return render(request, "AppLuis/circuito.html")

def clasificacion(request):
    return render(request, "AppLuis/clasificacion.html")


def crear_piloto(request):
    if request.method == "POST":
        piloto1 = Crear_piloto(request.POST)
        if piloto1.is_valid():
            info = piloto1.cleaned_data
            piloto1 = Crear_piloto(nombre = info["nombre"], apellido = info["apellido"], edad= ["edad"], correo= info["correo"])
            piloto1.save()
            return render( request, "AppLuis/crear_piloto.html")
    else:
        piloto1 = Crear_piloto()
    return render( request , "AppLuis/crear_piloto.html", {"pilot1":piloto1})


    
    
