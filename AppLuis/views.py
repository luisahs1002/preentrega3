from django.shortcuts import render, redirect
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
        form = Crear_piloto( request.POST)
        if form.is_valid():
            form.save()
        return redirect("INICIO")
    else:
        form = Crear_piloto()

    return render( request, "AppLuis/crear_piloto.html", {"piloto1":form})
    
def buscar_piloto(request):
    return render( request,"AppLuis/buscar_piloto.html")
        

    
def resultado_piloto(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        piloto_name = Piloto.objects.filter(nombre__icontains=nombre)
        return render(request, "AppLuis/resultadopiloto.html", {"valor_name" :nombre, "res" :piloto_name} )   

    return render( request, "AppLuis/resultadopiloto.html",)

#aca en el resultado esta mi error , no me aparece el resultado y me sale este error de la clase piloto en donde
#le di mil vueltas y aun haciendolo igual que el profe resultaba 


    


    
    
