from django.urls import path
from AppLuis.views import *



urlpatterns = [
    path("inicio/", inicio, name= "INICIO"),
    path("piloto/", piloto, name= "PILOTO"),
    path("scuderia/", scuderia, name= "SCUDERIA"),
    path("pista/", circuito, name="CIRCUITO"),
    path("clasificacion/", clasificacion, name = "CLASIFICACION"),
    path("crear_p/", crear_piloto, name="crear_piloto" ),

]
