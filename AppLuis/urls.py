from django.urls import path
from AppLuis.views import *
from django.contrib.auth.views import LogoutView



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
    path("crearcircuito/",crear_circuito, name="CREAR_CIRCUITO"),
    
    
    
    #buscar urls
    path("buscarpiloto",buscar_piloto, name="BUSCAR_PILOTO"),
    path("buscarscuderia/",buscar_scuderia, name="BUSCAR_SCUDERIA"),
    path("buscar_clasificacion/", buscar_clasificacion, name="BUSCAR_CLASIFICACION"),
    path("buscarcircuito/", buscar_circuito, name="BUSCAR_CIRCUITO"),
    
    #resultados urls
    path("resultadopiloto/",resultado_piloto, name="RESULTADO_PILOTO"),
    path("resultadoscuderia/",resultado_scuderia, name= "RESULTADO_SCUDERIA"),
    path("resultado_clasificacion/", resultado_clasificacion, name= "RESULTADO_CLASIFICACION"),
    path("resultadocircuito", resultado_circuito, name="RESULTADO_CIRCUITO"),

    # delete urls
    path("borrarpiloto/<nombre_piloto>/",eliminar_piloto,name="ELIMINAR_PILOTO"),
    path("borrarscuderia/<nombre_scuderia>/",eliminar_scuderia,name="ELIMINAR_SCUDERIA"),
    path("borrarclasificacion/<nombre_clasificacion>/", eliminar_clasificacion, name="ELIMINAR_CLASIFICACION"),
    path("borrarcircuito/<nombre_circuito>/",eliminar_circuito, name="ELIMINAR_CIRCUITO"),

    # Update urls
    path("editarpiloto/<nombre_piloto>/",actualizar_piloto, name="ACTUALIZAR_PILOTO"),
    path("editarscuderia/<nombre_scuderia>/",actualizar_scuderia, name="ACTUALIZAR_SCUDERIA"),
    path("editarclasificacion/<nombre_clasificacion>/",actualizar_clasificacion, name="ACTUALIZAR_CLASIFICACION"),
    path("editarcircuito/<nombre_circuito>/", actualizar_circuito, name="ACTUALIZAR_CIRCUITO"),

    #LOGIN, LOGOUT, REGISTRAR
    path("login/", login_view, name = "INICIO SESION"),
    path("registrar/", registrar, name="REGISTRAR"),
    path("logout/",LogoutView.as_view(template_name= "AppLuis/logout.html"),name="LOGOUT"),
    path("editar/",editar_usuario, name= "EDITAR"),

    # AVATAR
    path("avatar/", agregar_avatar, name="AGREGAR_AVATAR")







]
