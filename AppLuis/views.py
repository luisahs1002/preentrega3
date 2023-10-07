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

def crear_circuito(request):
    if request.method == "POST":
        form = Crear_circuito(request.POST)
        if form.is_valid():
            form.save()
        return redirect("INICIO")
    else:
        form = Crear_circuito()
    return render( request, "AppLuis/crear_circuito.html",{"formulario": form})





# READ
def buscar_piloto(request):
    return render( request,"AppLuis/buscar_piloto.html")
   
def resultado_piloto(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        piloto_name = Piloto.objects.filter(nombre__icontains=nombre)
        return render(request, "AppLuis/resultadopiloto.html", {"valor_name" :nombre, "res" :piloto_name} )   

    return render( request, "AppLuis/resultadopiloto.html",)




def buscar_scuderia(request):
    return render(request,"AppLuis/buscar_scuderia.html")

def resultado_scuderia(request):
    if request.GET['scuderia']:
        nombre = request.GET['scuderia']
        scuderia_name = Scuderia.objects.filter(scuderia__icontains=nombre)
        return render ( request, "AppLuis/resultado_scuderia.html",{"Nombre":nombre, "res2":scuderia_name})
   
    return render( request, "AppLuis/resultado_scuderia.html",) 

def buscar_clasificacion(request):
    return render(request, "AppLuis/buscar_clasificacion.html")

def resultado_clasificacion(request):
    if request.GET['circuito']:
        pista = request.GET['circuito']
        form = Clasificacion.objects.filter(circuito__icontains=pista)
        return render (request,"AppLuis/resultado_clasificacion.html",{'valor':pista, 'qualy':form})
    return render(request, "AppLuis/resultado_clasificacion.html")

def buscar_circuito(request):
    return render(request, "AppLuis/buscar_circuito.html")

def resultado_circuito(request):
    if request.GET['circuito']:
        pista = request.GET['circuito']
        form = Circuito.objects.filter(circuito__icontains=pista)
        return render(request,"AppLuis/resultado_circuito.html", {"valor":pista , 'form':form})
    return render(request, "AppLuis/resultado_circuito.html")


#INICIO/ALL
def inicio(request):
    return render(request, "AppLuis/inicio.html")

def piloto(request):
    all_pilotos = Piloto.objects.all()
    return render(request, "AppLuis/piloto.html", {'pilotos': all_pilotos})

def scuderia(request):
    contexto = Scuderia.objects.all()
    return render(request, "AppLuis/scuderia.html", {'scuderias': contexto})

def circuito(request):
    all_circuitos = Circuito.objects.all()
    return render(request, "AppLuis/circuito.html", {"circuitos": all_circuitos})

def clasificacion(request):
    all_clasificacion = Clasificacion.objects.all()
    return render( request, "AppLuis/clasificacion.html", {'clasificaciones':all_clasificacion})


# DELETE
def eliminar_piloto(request, nombre_piloto):
    piloto_escogido = Piloto.objects.get(nombre=nombre_piloto)
    piloto_escogido.delete()
    todos = Piloto.objects.all()
    return render(request, "AppLuis/piloto.html", {'pilotos': todos})

def eliminar_scuderia(request, nombre_scuderia):
    scuderia_escogido = Scuderia.objects.get(scuderia=nombre_scuderia)
    scuderia_escogido.delete()
    todos = Scuderia.objects.all()
    return render(request, "AppLuis/scuderia.html", {'scuderias': todos})

def eliminar_clasificacion( request, nombre_clasificacion):
    clasificacion_escogido = Clasificacion.objects.get(clasificacion=nombre_clasificacion)
    clasificacion_escogido.delete()
    todos = Clasificacion.objects.all()
    return render ( request, "AppLuis/clasificacion.html",{'clasificaciones' : todos})

def eliminar_circuito(request, nombre_circuito):
    circuito_escogido = Circuito.objects.get(circuito=nombre_circuito)
    circuito_escogido.delete()
    todos = Circuito.objects.all()
    return render ( request, "AppLuis/circuito.html",{'circuitos': todos})

#UPDATE 
def actualizar_piloto(request, nombre_piloto):
     piloto_escogido = Piloto.objects.get(nombre=nombre_piloto)
     if request.method == "POST":
            form = Crear_piloto( request.POST)
            if form.is_valid():
                info = form.cleaned_data
                piloto_escogido.nombre = info['nombre']
                piloto_escogido.apellido = info['apellido']
                piloto_escogido.edad = info['edad']
                piloto_escogido.correo = info['correo']

                piloto_escogido.save()
                return redirect("INICIO")
     else:
        form = Crear_piloto(initial={"nombre":piloto_escogido.nombre,
                                     "apellido":piloto_escogido.apellido,
                                     "edad":piloto_escogido.edad,
                                     "correo":piloto_escogido.correo})

        return render ( request, "AppLuis/editar_piloto.html",{"formulario":form})

def actualizar_scuderia(request, nombre_scuderia):
    scuderia_escogido = Scuderia.objects.get(scuderia=nombre_scuderia)
    if request.method == "POST":
        form = Crear_scuderia(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            scuderia_escogido.scuderia = info["scuderia"]
            scuderia_escogido.save()
            return redirect("INICIO")
    else:
        form = Crear_scuderia(initial={"scuderia":scuderia_escogido.scuderia})
        return render( request, 'AppLuis/editar_scuderia.html', {"formulario":form})
    

def actualizar_clasificacion(request, nombre_clasificacion):
    clasificacion_escogido = Clasificacion.objects.get(tiempo=nombre_clasificacion)
    if request.method == "POST":
        form = Crear_clasificacion(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            clasificacion_escogido.nombre_apellido = info["nombre_apellido"]
            clasificacion_escogido.circuito = info["circuito"]
            clasificacion_escogido.tiempo = info["tiempo"]
            clasificacion_escogido.save()
            return redirect("INICIO")
    else:
        form = Crear_clasificacion(initial={"nombre_apellido":clasificacion_escogido.nombre_apellido,
                                            "circuito":clasificacion_escogido.circuito,
                                            "tiempo":clasificacion_escogido.tiempo})
        return render(request, "AppLuis/editar_clasificacion.html",{"formulario":form})
    
def actualizar_circuito(request, nombre_circuito):
    circuito_escogido = Circuito.objects.get(circuito=nombre_circuito)
    if request.method == "POST":
        form = Crear_circuito(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            circuito_escogido.circuito = info['circuito']
            circuito_escogido.tiempo = info['tiempo']
            circuito_escogido.save()
            return redirect("INICIO")
    else:
        form = Crear_circuito(initial={"circuito":circuito_escogido.circuito,
                                       "tiempo":circuito_escogido.tiempo})
        return render(request, "AppLuis/editar_circuito.html",{"formulario": form })
