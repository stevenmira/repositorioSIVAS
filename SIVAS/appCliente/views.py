from django.shortcuts import render, redirect
from appAdminAeropuerto.forms import *
from appAdminAplicacion.models import *
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView

)

# Create your views here.

def index(request):
	return render(request,"cliente/index.html")


#funcion que busca los vuelos
def busqueda(request):
	ciudades = ciudad.objects.all()

	if request.method == 'POST':
		ciudad_origen =ciudad.objects.filter(cod_iata_ciudad=request.POST.get('ciudadOrigen')) 
		ciudad_destino = ciudad.objects.filter(cod_iata_ciudad=request.POST.get('ciudadDestino'))

		aero_origen = aeropuerto.objects.filter(ciudad=ciudad_origen)
		aero_destino = aeropuerto.objects.filter(ciudad=ciudad_destino)

		vuelo_principal = vuelo.objects.filter(aeropuerto_origen=aero_origen,aeropuerto_destino=aero_destino)

		if vuelo_principal is None:
			pass
		else:
			itinerario_principal = itinerario.objects.filter(vuelo = vuelo_principal)
		


		