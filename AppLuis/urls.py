from django.urls import path
from AppLuis.views import *



urlpatterns = [
    path("inicio/", inicio, name= "INICIO"),
    path("piloto/", piloto, name= "PILOTO"),
    path("scuderia/", scuderia, name= "SCUDERIA"),
    path("pista/", circuito, name="CIRCUITO"),
    path("clasificacion/", clasificacion, name = "CLASIFICACION"),
    #crear urls
    path("crear_piloto/", crear_piloto, name="CREAR_PILOTO"),
    path("crearscuderia/", crear_scuderia, name="CREAR_SCUDERIA"),
    path("crear_qualy/", crear_clasificacion, name= "CREAR_CLASIFICACION"),
    
    
    
    #buscar urls
    path("buscarpiloto",buscar_piloto, name="BUSCAR_PILOTO"),
    path("buscarscuderia/",buscar_scuderia, name="BUSCAR_SCUDERIA"),
    path("buscar_clasificacion/", buscar_clasificacion, name="BUSCAR_CLASIFICACION"),
    
    #resultados urls
    path("resultadopiloto/",resultado_piloto, name="RESULTADO_PILOTO"),
    path("resultadoscuderia/",resultado_scuderia, name= "RESULTADO_SCUDERIA"),
    path("resultado_clasificacion/", resultado_clasificacion, name= "RESULTADO_CLASIFICACION"),

    # delete urls
    path("borrarpiloto/<nombre_piloto>/",eliminar_piloto,name="ELIMINAR_PILOTO"),
    path("borrarscuderia/<nombre_scuderia>/",eliminar_scuderia,name="ELIMINAR_SCUDERIA"),
    path("borrarclasificacion/<nombre_clasificacion>/", eliminar_clasificacion, name="ELIMINAR_CLASIFICACION"),

    # Update urls
    path("editarpiloto/<nombre_piloto>/",actualizar_piloto, name="ACTUALIZAR_PILOTO"),





]
