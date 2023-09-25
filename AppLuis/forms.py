from django import forms
from .models import Piloto


class Crear_piloto(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre', 'apellido', 'edad', 'correo']


