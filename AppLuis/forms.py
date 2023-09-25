from django import forms
from .models import *


class Crear_piloto(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre', 'apellido', 'edad', 'correo']

class Crear_scuderia(forms.ModelForm):
    class Meta:
        model = Scuderia
        fields = ['scuderia']

class Crear_clasificacion(forms.ModelForm):
    class Meta:
        model = Clasificacion
        fields = ['nombre_apellido', 'circuito', 'tiempo']
        
