from django.urls import path
from AppLuis.views import *



urlpatterns = [
    path("inicio/", inicio, name= "INICIO"),
    path("piloto/", piloto, name= "PILOTO"),
    path("scuderia/", scuderia, name= "SCUDERIA"),
    path("pista/", circuito, name="CIRCUITO"),
    path("clasificacion/", clasificacion, name = "CLASIFICACION"),
    path("crear_piloto/", crear_piloto, name="CREAR_PILOTO"),
    path("buscarpiloto",buscar_piloto, name="BUSCAR_PILOTO"),
    path("resultadopiloto",resultado_piloto, name="RESULTADO_PILOTO"),
    path("crearscuderia/", crear_scuderia, name="CREAR_SCUDERIA"),
    path("buscarscuderia/", buscar_scuderia, name="BUSCAR_SCUDERIA"),
    path("resultadoscuderia/", resultado_scuderia, name= "RESULTADO_SCUDERIA"),
    path("crear_qualy/", crear_clasificacion, name= "CREAR_CLASIFICACION"),
    path("buscar_clasificacion/", buscar_clasificacion, name="BUSCAR_CLASIFICACION"),
    path("resultado_clasificacion/", resultado_clasificacion, name= "RESULTADO_CLASIFICACION"),



]
