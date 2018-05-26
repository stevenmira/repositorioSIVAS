from django import forms
from appAdminAplicacion.models import *

class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = aeropuerto
        exclude = ()
        field = [
            'nombre_aeropuerto',
            'telefono_aeropuerto',
            'nombre_responsable',
            'ciudad',
            
        ]
        widgets = {
            'nombre_aeropuerto':forms.TextInput(attrs={'class':'form-control','placeholder':'Introduzca el nombre del Aeropuerto','autofocus':'True','required':'True','maxlenght':'50'}),
            'telefono_aeropuerto':forms.TextInput(attrs={'class':'form-control','placeholder':'Numero telefonico principal','autofocus':'True','required':'True','maxlength':'15'}),
            'nombre_responsable':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre del responsable','autofocus':'True','required':'True','maxlenght':'50'}),   
        }