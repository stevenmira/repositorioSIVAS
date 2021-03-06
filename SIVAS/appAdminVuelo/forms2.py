from django import forms

from appAdminAplicacion.models import *


class TipoAvionForm(forms.ModelForm):
	
	class Meta:
		model = tipo_avion
		exclude = ()
		field = [
			'nombre_tipo_avion',
		]
		widgets = {
			'nombre_tipo_avion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca el Tipo','autofocus':'True', 'required':'True', 'maxlength':'30'}),
			
		}

class AvionForm(forms.ModelForm):
	
	class Meta:
		model = avion
		exclude = ()
		field = [
			'linea_aerea',
			'modelo',
			'marca',
			'capacidad_asientos',
		]
		widgets = {
			'linea_aerea': forms.TextInput(attrs={'class':'form-control', 'type':'hidden'}),
			'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca el modelo', 'required':'True', 'maxlength':'30'}),
			'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca el marca', 'autofocus':'True', 'required':'True', 'maxlength':'20'}),
			'capacidad_asientos': forms.NumberInput(attrs={'class':'form-control','placeholder':'(sin espacio)', 'required':'True'}),
		} 

class TipoCabinaForm(forms.ModelForm):
	
	class Meta:
		model = tipo_cabina
		exclude = ()
		field = [
			'nombre_cabina',
		]
		widgets = {
			'nombre_cabina': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca el nombre', 'required':'True', 'maxlength':'30'}),
		}

class DetalleClaseForm(forms.ModelForm):
	
	class Meta:
		model = detalle_clase
		exclude = ()
		field = [
			'cantidad_asientos',
			'stock',
			'conf_columnas',
			'conf_filas',
			'avion',
		]
		widgets = {
			'cantidad_asientos': forms.NumberInput(attrs={'class':'form-control', 'placeholder':' . . .', 'required':'True', 'autofocus':'True'}),
			'stock': forms.NumberInput(attrs={'class':'form-control'}),
			'conf_columnas': forms.TextInput(attrs={'class':'form-control','data-inputmask':'"mask": "9-9-9"','data-mask':'on', 'maxlength':'10', 'requerid':'True'}),
			'conf_filas': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'No. filas', 'required':'True'}),
			'avion': forms.TextInput(attrs={'required':'False', 'type':'hidden', 'value':'1'}),
		}

class AsientoForm(forms.ModelForm):
	
	class Meta:
		model = avion
		exclude = ()
		field = [
			'fila',
			'columna',
			'estado_asiento',
		]
		widgets = {
			'fila': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'#', 'required':'True', 'autofocus':'True'}),
			'columna': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Letra . . .',  'required':'True', 'maxlength':'10'}),
			'estado_asiento': forms.TextInput(attrs={'class':'form-control', 'maxlength':'15'}),
		}

class VueloForm(forms.ModelForm):
	
	class Meta:
		model = vuelo
		exclude = ()
		field = [
			'codigo_vuelo'
			'aeropuerto_origen',
			'aeropuerto_destino',
			'costo_viaje',
			'milla_recorrida',
			'milla_otorgar',
			'tiempo_de_vuelo',
			'linea_aerea',
		]
		widgets = {
			'codigo_vuelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej. AV010', 'required':'True', 'maxlength':'15', 'readonly':'True'}),
			'costo_viaje': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Costo...', 'required':'True', 'min':'1', 'max':'999999'}),
			'milla_recorrida': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'No. M.R', 'required':'True', 'min':'1', 'max':'99999'}),
			'milla_otorgar': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'No. M.O', 'required':'True', 'min':'1', 'max':'99999'}),
			'tiempo_de_vuelo': forms.TextInput(attrs={'class':'form-control', 'type':'time', 'required':'True'}),
		}

