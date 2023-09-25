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

]
