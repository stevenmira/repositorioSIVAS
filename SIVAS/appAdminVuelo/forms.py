from django import forms
from appAdminAplicacion.models import *


class LineaForm(forms.ModelForm):
    class Meta:
        model = linea_aerea
        exclude = ()
        field = [
            'codigo_linea_aerea',
            'pais',
            'nombre_oficial',
            'nombre_corto'
            'fecha_fundacion',
            'nombre_representante',
            'direccion_facebook',
            'direccion_twitter',
            'email_linea_aerea',
        ]
        widgets = dict(
            codigo_linea_aerea=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca el codigo', 'autofocus': 'True',     'requerid': 'True', 'maxlength': '10'}),
            pais=forms.Select(attrs={'class': 'form-control'}),
            nombre_oficial=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca nombre oficial','autofocus': 'True','requerid': 'True', 'maxlength': '50'}),
            nombre_corto=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca nombre corto', 'autofocus': 'True','requerid': 'True', 'maxlength': '30'}),
            fecha_fundacion=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            nombre_representante=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca nombre del representante','autofocus': 'True','requerid': 'True', 'maxlength': '50'}),
            direccion_facebook=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: https://www.facebook.com/MiPerfil', 'autofocus': 'True','requerid': 'True', 'maxlength': '30'}),
            direccion_twitter=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: @MiPerfil', 'autofocus': 'True','requerid': 'True', 'maxlength': '30'}),
            email_linea_aerea=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca Correo', 'autofocus': 'True','maxlength': '255'}))
