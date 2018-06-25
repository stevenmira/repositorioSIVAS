from django.shortcuts import render, redirect
from appAdminAplicacion.models import *

def bienvenido(request):
	aeropuertos = aeropuerto.objects.all()
	msj=0

	if request.method == 'POST':
		origen  =  request.POST['aeropuerto_origen']
		destino = request.POST['aeropuerto_destino']
		salida = request.POST['salida']
		regreso = request.POST['regreso']
		#escalas = request.POST['escalas']

		if origen == destino:
			msj = 'El aeropuerto destino debe ser diferente del aeropuerto de origen'
			return render(request,"reserva/bienvenido.html",{'aeropuertos':aeropuertos, 'msj': msj})

		if salida > regreso:
			msj = 'La fecha de salida debe ser menor que la fecha de regreso'
			return render(request,"reserva/bienvenido.html",{'aeropuertos':aeropuertos, 'msj': msj})

		a = aeropuerto.objects.get(codigo_aeropuerto=origen)
		b = aeropuerto.objects.get(codigo_aeropuerto=destino)

		itiSalida = itinerario.objects.filter(aeropuert_origen__codigo_aeropuerto=origen, 
			aeropuert_destino__codigo_aeropuerto=destino)

		cont =len(itiSalida)

		diccionario={}
		for i in range(cont):
			pkp = itiSalida[i].id_itinerario
			iti = itinerario.objects.get(id_itinerario = pkp)
			detalles = detalle_itinerario.objects.filter(itinerario = iti)
			diccionario[iti]=[detalles]

		return render(request,"reserva/itinerarios.html",{'diccionario':diccionario, 
			'salida':salida, 'regreso':regreso, 'a':a, 'b':b })
			
	return render(request,"reserva/bienvenido.html",{'aeropuertos':aeropuertos, 'msj':msj})

def llegada(request):

	if request.method == 'POST':
		origen = request.POST['b']
		destino  =  request.POST['a']
		salida = request.POST['f1']
		regreso = request.POST['f2']

		a = aeropuerto.objects.get(codigo_aeropuerto=origen)
		b = aeropuerto.objects.get(codigo_aeropuerto=destino)

		# Ahora es al reves la consulta
		itiSalida = itinerario.objects.filter(aeropuert_origen__codigo_aeropuerto=origen, 
			aeropuert_destino__codigo_aeropuerto=destino)

		cont =len(itiSalida)

		diccionario={}
		for i in range(cont):
			pkp = itiSalida[i].id_itinerario
			iti = itinerario.objects.get(id_itinerario = pkp)
			detalles = detalle_itinerario.objects.filter(itinerario = iti)
			diccionario[iti]=[detalles]

		return render(request,"reserva/llegada.html",{'diccionario':diccionario, 
			'salida':salida, 'regreso':regreso, 'a':a, 'b':b })