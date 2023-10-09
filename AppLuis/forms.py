from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


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

class Crear_circuito(forms.ModelForm):
    class Meta:
        model = Circuito
        fields = ['circuito','tiempo']

class registrarse(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Editar_registro(UserCreationForm):
     email = forms.EmailField()
     
     class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2'] 

class avatar_formulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"



        

        


        
