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
            'ciudad' : forms.Select(attrs={'class':'form-control'}),
        }


class PaisForm(forms.ModelForm):
    class Meta:
        model = pais
        exclude = ()
        field = [
            'nombre_pais',
            'cod_iata_pais',
        ]
        widgets = {
            'nombre_pais':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Nombre del Pais','autofocus':'True','required':'True','maxlength':'30'}),
            'cod_iata_pais':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Codigo IATA','autofocus':'True','required':'True','maxlenght':'2'})
        }


class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        exclude = ()
        field = [
            'pais',
            'cod_iata_ciudad',
            'nombre_ciudad',
        ]
        widgets = {
            'pais':forms.Select(attrs={'class':'form-control'}),
            'cod_iata_ciudad':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Codigo IATA de la ciudad','autofocus':'True','required':'True','maxlenght':'3'}),
            'nombre_ciudad':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre de la Ciudad','autofocus':'true','required':'true','maxlenght':'30'}),
        }

class EstadoCivilForm(forms.ModelForm):
    class Meta:
        model = estado_civil
        exclude = ()
        field = [
            'nombre_estado',
        ]
        widgets = {
            'nombre_estado':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Nombre del Estado Civil','autofocus':'True','required':'True','maxlength':'15'}),
            
        }

class GeneroForm(forms.ModelForm):
    class Meta:
        model = genero
        exclude = ()
        field = [
            'nombre_genero',
        ]
        widgets = {
            'nombre_genero':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Genero','autofocus':'True','required':'True','maxlength':'1'}),
            
        }

class TipoForm(forms.ModelForm):
    class Meta:
        model = tipo_documento
        exclude = ()
        field = [
            'nombre_tipo_documento',
        ]
        widgets = {
            'nombre_tipo_documento':forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el Tipo de Documento','autofocus':'True','required':'True','maxlength':'20'}),
            
        }