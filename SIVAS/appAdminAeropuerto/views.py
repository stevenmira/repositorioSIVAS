from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from appAdminAeropuerto.forms import *
from appAdminAplicacion.models import *


from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView

)

def index(request):
    return render(request,"general/index.html")


def aeropuerto_create(request):

    if request.method == 'POST':
        form = AeropuertoForm(request.POST)
        if form.is_valid():
            num = aeropuerto.objects.filter(ciudad = form.cleaned_data['ciudad'])
            count = len(num)
            codigo = form.cleaned_data['ciudad']
            if count == 0:


                aerox = aeropuerto(
                    ciudad = form.cleaned_data['ciudad'],
                    nombre_aeropuerto = form.cleaned_data['nombre_aeropuerto'],
                    telefono_aeropuerto = form.cleaned_data['telefono_aeropuerto'],
                    nombre_responsable = form.cleaned_data['nombre_responsable'],
                    codigo_aeropuerto = codigo.cod_iata_ciudad+str(count+1))
                aerox.save()
                return redirect('aaae:listaPais')

            else:
                aerox = aeropuerto(
                    ciudad = form.cleaned_data['ciudad'],
                    nombre_aeropuerto = form.cleaned_data['nombre_aeropuerto'],
                    telefono_aeropuerto = form.cleaned_data['telefono_aeropuerto'],
                    nombre_responsable = form.cleaned_data['nombre_responsable'],
                    codigo_aeropuerto = codigo.cod_iata_ciudad+str(count+1))
                aerox.save()
                return redirect('aaae:listaPais')
        else:
            return render(request, 'aero/aeropuertoCreate.html', {'form':form})
    else:
        form = AeropuertoForm()
    return render(request, 'aero/aeropuertoCreate.html', {'form':form})


def pais_create(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if  form.is_valid():
            paisx = pais(
                
                nombre_pais = form.cleaned_data['nombre_pais'],
                cod_iata_pais = form.cleaned_data['cod_iata_pais'],
            )
            paisx.save()
            return redirect('aaae:listaPais')
        else:
             return render(request,'pais/paisCreate.html',{'form':form})
    else:
        form = PaisForm
    return render(request,'pais/paisCreate.html',{'form':form})

class AeroList(ListView):
    model = aeropuerto
    template_name = "aero/listaAeropuerto.html"
    paginate_by = 10

class AeroUpdate(UpdateView):
    model = aeropuerto
    form_class = AeropuertoForm
    template_name = "aero/aeroUpdate.html"
    success_url = reverse_lazy('aaae:listaAero')

class AeroDelete(DeleteView):
    model = aeropuerto
    template_name = "aero/aeroDelete.html"
    success_url = reverse_lazy('aaae:listaAero')


def ciudad_create(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if  form.is_valid():
            ciudadx = ciudad(
                pais = form.cleaned_data['pais'],
                cod_iata_ciudad = form.cleaned_data['cod_iata_ciudad'],
                nombre_ciudad = form.cleaned_data['nombre_ciudad'],
            )
            ciudadx.save()
        return redirect ('aaae:listaCiudad')
    else:
        form = CiudadForm()
    return render(request,'ciudad/ciudadCreate.html',{'form':form})

def curso_exito(request):
    return render(request,'exito.html',None)

class PaisList(ListView):
    model = pais
    template_name = "pais/listaPaises.html"
    paginate_by = 10

class PaisUpdate(UpdateView):
    model = pais
    form_class = PaisForm
    template_name = "pais/paisUpdate.html"
    success_url = reverse_lazy('aaae:listaPais')

class PaisDelete(DeleteView):
    model = pais
    template_name = "pais/paisDelete.html"
    success_url = reverse_lazy('aaae:listaPais')

class CiudadList(ListView):
    model = ciudad
    template_name = "ciudad/listaCiudades.html"
    paginate_by = 10

class CiudadUpdate(UpdateView):
    model = ciudad
    form_class = CiudadForm
    template_name = "ciudad/ciudadUpdate.html"
    success_url = reverse_lazy('aaae:listaCiudad')

class CiudadDelete(DeleteView):
    model = ciudad
    template_name = "ciudad/ciudadDelete.html"
    success_url = reverse_lazy('aaae:listaCiudad')

'''
class ciudad_create(CreateView):
    model = ciudad
    form_class = CiudadForm
    template_name = "ciudad/ciudadCreate.html"
    success_url = reverse_lazy('aaae:listaPais')
'''