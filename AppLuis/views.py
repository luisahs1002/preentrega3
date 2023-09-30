from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppLuis.models import * 
from django.template import Template, loader
from AppLuis.forms import *


# Create 

def crear_piloto(request):
    if request.method == "POST":
        form = Crear_piloto( request.POST)
        if form.is_valid():
            form.save()
        return redirect("INICIO")
    else:
        form = Crear_piloto()

    return render( request, "AppLuis/crear_piloto.html", {"piloto1":form})


def crear_scuderia(request):
    if request.method == "POST":
        form = Crear_scuderia(request.POST)
        if form.is_valid():
            form.save()
        return redirect("INICIO")
    else:
        form = Crear_scuderia()
    return render( request, "AppLuis/crear_scuderia.html", {"scuderia1":form})

def crear_clasificacion(request):
    if request.method == "POST":
        form = Crear_clasificacion(request.POST)
        if form.is_valid():
            form.save()
        return redirect("INICIO")
    else:
        form = Crear_clasificacion()
    return render( request, "AppLuis/crear_clasificacion.html", {"qualy":form})




# READ
def buscar_piloto(request):
    return render( request,"AppLuis/buscar_piloto.html")
   
def resultado_piloto(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        piloto_name = Piloto.objects.filter(nombre__icontains=nombre)
        return render(request, "AppLuis/resultadopiloto.html", {"valor_name" :nombre, "res" :piloto_name} )   

    return render( request, "AppLuis/resultadopiloto.html",)

def piloto(request):
    all_pilotos = Piloto.objects.all()
    return render(request, "AppLuis/piloto.html", {'pilotos': all_pilotos})


def buscar_scuderia(request):
    return render(request,"AppLuis/buscar_scuderia.html")

def resultado_scuderia(request):
    if request.GET['scuderia']:
        nombre = request.GET['scuderia']
        scuderia_name = Scuderia.objects.filter(scuderia__icontains=scuderia)
        return render ( request, "AppLuis/resultado_scuderia.html", {"valor":nombre, "res2":scuderia_name})
    return render( request, "AppLuis/resultado_scuderia.html")

def equipos(request):
    pass

def buscar_clasificacion(request):
    return render(request, "AppLuis/buscar_clasificacion.html")

def resultado_clasificacion(request):
    if request.GET['nombre_apellido']:
        nombre = request.GET['nombre_apellido']
        form = Clasificacion.objects.filter(clasificacion__icontains=clasificacion)
        return render (request,"AppLuis/resultado_clasificacion.html", {'valor':nombre, 'qualy':form})
    return render(request, "AppLuis/resultado_clasificacion.html")

def CLASIFICACION(request):
    all_clasificacion = Clasificacion.objects.all()
    return render( request, "AppLuis/clasificacion.html", {'clasificaciones':all_clasificacion})
#INICIO
def inicio(request):
    return render(request, "AppLuis/inicio.html")



def scuderia(request):
    contexto = Scuderia.objects.all()
    return render(request, "AppLuis/scuderia.html", {'scuderias': contexto})

def circuito(request):
    return render(request, "AppLuis/circuito.html")

def clasificacion(request):
    return render(request, "AppLuis/clasificacion.html")



    
