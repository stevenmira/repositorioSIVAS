from django.shortcuts import render
from appAdminAeropuerto.models import *
from appAdminAeropuerto.forms import *
from django.shortcuts import render, redirect
from appAdminAeropuerto.forms import *
from appAdminAplicacion.models import *
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import time

from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView

)

# Create your views here.

def index(request):
	return render(request,"cliente/index.html")



def register(request):
	gene=genero.objects.all()
	tidoc=tipo_documento.objects.all()
	esta=estado_civil.objects.all()
	if request.method == 'POST':

		nam1=request.POST['primer_nombre']
		nam2=request.POST['segundo_nombre']
		apell1=request.POST['primer_apellido']
		apell2=request.POST['segundo_apellido']
		numedoc=request.POST['numero_documento']
		telefijo=request.POST['telefono_fijo']
		telemovi=request.POST['telefono_movil']
		emailx=request.POST['email_pasajero']
		pas=request.POST['psw']
		gen=request.POST['genero']
		tip=request.POST['tipo']
		est=request.POST['estado']
		fech=request.POST['fecha']
		gener = genero.objects.get(id_genero=gen)
		tipo_document = tipo_documento.objects.get(id_tipo_documento=tip)
		estado_civi = estado_civil.objects.get(id_estado_civil=est)

		#Primero ingresamos el usuario a Django
		usuario=User(username=request.POST["nameus"],email=emailx)
		usuario.set_password(pas)
		usuario.save()

		us=User.objects.latest('id')
		#Luego se ingresa el usuario a la tabla Pasajero
		cliente = cliente_natural.objects.create(numero_documento=numedoc,genero=gener,tipo_documento=tipo_document,estado_civil=estado_civi,fecha_nacimiento=fech)
		pasajero.objects.create(numero_viajero=numedoc,cliente_natural=cliente,primer_nombre=nam1,segundo_nombre=nam2,primer_apellido=apell1,segundo_apellido=apell2,telefono_fijo=telefijo,telefono_movil=telemovi,email_pasajero=emailx,user_id=us)
		return render(request, "cliente/congratulation.html")
	context={
		'genero':gene,
		'tipodoc':tidoc,
		'estado':esta,
	}

	return render(request,"cliente/register.html",context)

def register_emp(request):
	if request.method == 'POST':
		nam1=request.POST['primer_nombre']
		nam2=request.POST['segundo_nombre']
		apell1=request.POST['primer_apellido']
		apell2=request.POST['segundo_apellido']
		nomemp=request.POST['nombre_empresa']
		numedoc=request.POST['numero_documento']
		nomcon=request.POST['nombre_contacto']
		nic=request.POST['nic_empresa']
		telefijo=request.POST['telefono_fijo']
		telemovi=request.POST['telefono_movil']
		email=request.POST['email_pasajero']
		pas=request.POST['psw']
		
		usuario=User(username=request.POST["nameus"],email=email)
		usuario.set_password(pas)
		usuario.save()
		us=User.objects.latest('id')
		
		cliente = cliente_empresa.objects.create(nit=numedoc,nombre_empresa=nomemp,nic_empresa=nic,nombre_contacto=nomcon)
		pasajero.objects.create(numero_viajero=numedoc,cliente_empresa=cliente,primer_nombre=nam1,segundo_nombre=nam2,primer_apellido=apell1,segundo_apellido=apell2,telefono_fijo=telefijo,telefono_movil=telemovi,email_pasajero=email,user_id=us)
		return render(request, "cliente/congratulation.html")

	return render(request,"cliente/registeremp.html")

def before(request):
	return render(request,"cliente/before.html")

def ingreso(request):
	if request.method == 'POST':

		email = request.POST['email_pasajero']
		pas=request.POST['psw']

		user = authenticate(username=email,password=pas)

		if user is not None:
			login(request,user)
			return render(request,"cliente/welcome.html")
		else:
			print("Esto es Nulo :c")
			alert=1
			context={
				"alert":alert,
			}
			return render(request, "cliente/ingreso.html",context)
	return render(request, "cliente/ingreso.html")




def indexBusqueda(request):
	ciudades = ciudad.objects.all()
	return render(request,"reserva/inicio.html",{'ciudades':ciudades})

#funcion que busca los vuelos
def busqueda(request):

	if request.method == 'POST':

		ciudades = ciudad.objects.all()

		if request.method == 'POST':
			ciudad_origen =ciudad.objects.filter(cod_iata_ciudad=request.POST.get('ciudadOrigen')) 
			ciudad_destino = ciudad.objects.filter(cod_iata_ciudad=request.POST.get('ciudadDestino'))
			fecha_partida = request.POST.get('fecha_partida')
			fecha_regreso = request.POST.get('fecha_regreso')
			aero_origen = aeropuerto.objects.filter(ciudad=ciudad_origen)
			aero_destino = aeropuerto.objects.filter(ciudad=ciudad_destino)

			#vuelo_principal = vuelo.objects.filter(aeropuerto_origen=aero_origen,aeropuerto_destino=aero_destino)
			itinerarios_partida = itinerario.objects.filter(aeropuert_origen=aero_origen,aeropuert_destino=aero_destino, fecha_itinerario=fecha_partida).select_related()

			#vuelo_principal = vuelo.objects.filter(aeropuerto_origen=aero_origen,aeropuerto_destino=aero_destino)
			itinerarios_partida = itinerario.objects.filter(aeropuert_origen=aero_origen,aeropuert_destino=aero_destino, fecha_itinerario=fecha_partida)
			itinerarios_regreso = itinerario.objects.filter(aeropuert_origen= aero_origen, aeropuert_destino=aero_destino,fecha_itinerario=fecha_regreso)
			if itinerario_partida is None or itinerarios_regreso is None:
				msg="No se encontro vuelos para esas fechas, por favor verigique con otras fechas"
				return render(request,"reserva/inicio.html",{'MSG':msg})
			else:
				return render(request,"reserva/resultado.html",{'salidas':itinerario_partida,'regresos':itinerarios_regreso})

			itinerarios_regreso = itinerario.objects.filter(aeropuert_origen= aero_origen, aeropuert_destino=aero_destino,fecha_itinerario=fecha_regreso)
			if itinerario_partida is None or itinerarios_regreso is None:
				msg="No se encontro vuelos para esas fechas, por favor verigique con otras fechas"
				return render(request,"reserva/inicio.html",{'MSG':msg})
			else:
				return render(request,"reserva/resultado.html",{'salidas':itinerario_partida,'regresos':itinerarios_regreso})
				
	else:
		ciudades = ciudad.objects.all()
	return render(request,"reserva/inicio.html",{'ciudades':ciudades})

def perfil(request):
	client = pasajero.objects.get(user_id=request.user.id)
	tarje = tarjeta.objects.filter(pasajero=client)
	detall_rese = detalle_reservacion.objects.filter(numero_viajero=client)

	lista = []
	#print(detall_rese)
	for deta in detall_rese:
		reserva = reservacion.objects.get(codigo_reservacion=deta.codigo_reservacion.codigo_reservacion)
		detall_via = detalle_viaje.objects.filter(reservacion=reserva)
		for detavia in detall_via:
			iti = itinerario.objects.get(id_itinerario=detavia.itinerario.id_itinerario)
			try:
				pagoo = pago.objects.get(reservacion=reserva)
				pag = pagoo.estado_pago
			except Exception as e:
				pag="No hay informacion"
			
			print(pag)
			if pag == "Activo":
				xs=[reserva.codigo_reservacion,detavia.bin_tipo,reserva.fecha_salida,reserva.fecha_regreso,iti.monto_total,"Pagado"]
			else:
				xs=[reserva.codigo_reservacion,detavia.bin_tipo,reserva.fecha_salida,reserva.fecha_regreso,iti.monto_total,"No Pagado"]
			lista.append(xs)
	
	context={
		"cliente":client,
		"tarjeta":tarje,
		"list":lista,
	}
	return render(request, "cliente/perfil.html",context)

def logoute(request):
	logout(request)
	return redirect('/ingreso')

def tarjet(request):
	pasaje = pasajero.objects.get(user_id=request.user.id)
	tipo = tipo_tarjeta.objects.all()
	if request.method == 'POST':
		num = request.POST['numero_tarjeta']
		nom = request.POST['nombre_tarjeta']
		ven = request.POST['vencimiento']
		tip = request.POST['tipo']
		print(tip)
		tipox = tipo_tarjeta.objects.get(id_tipo_tarjeta=tip)

		tarjet = tarjeta.objects.create(tipo_tarjeta=tipox,pasajero=pasaje,numero_tarjeta=num,nombre_tarjeta=nom,vencimiento=ven)
		return render(request,"tarjeta/exito.html")
	context = {
		"tipo":tipo,
	}
	return render(request, "tarjeta/asignarTarjeta.html", context)


def pagox(request,pk):
	acumulador=0
	reser = reservacion.objects.get(codigo_reservacion=pk)
	detall_via = detalle_viaje.objects.filter(reservacion=reser)
	pasa = pasajero.objects.get(user_id=request.user.id)
	tarjes = tarjeta.objects.filter(pasajero=pasa)
	for detavia in detall_via:
		iti = itinerario.objects.get(id_itinerario=detavia.itinerario.id_itinerario)
		acumulador = acumulador+iti.monto_total
		print(acumulador)

	if request.method ==  'POST':
		estado = "Activo"
		datee = time.strftime("%Y-%m-%d")
		print(datee)
		acum = acumulador
		tagge=request.POST['tarjett']
		tar = tarjeta.objects.get(id_tarjeta=tagge)

		pags=pago.objects.create(tarjeta=tar,reservacion=reser,cantidad_pago=acum,fecha_pago=datee,estado_pago=estado)
		
		return render(request,"pago/exito.html")
	context={
		"acmu":acumulador,
		"targ":tarjes,
	}

	return render(request,"pago/realizarPago.html",context)