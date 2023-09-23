from django import forms


class Crear_piloto(forms.Form):
    nombre= forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    correo = forms.EmailField()


