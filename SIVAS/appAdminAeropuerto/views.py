from django.shortcuts import render, redirect
from django.http import HttpResponse
from appAdminAeropuerto.forms import *

from django.views.generic.list import ListView

def index(request):
    return render(request,"general/index.html")


def aeropuerto_create(request):
    if request.method == 'POST':
        form = AeropuertoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('appCliente: index')
    else:
        form = AeropuertoForm()
    return render(request, 'aeropuertoCreate.html', {'form':form})

def pais_create(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if  form.is_valid():
            paisx = pais(
                codigo_pais =1,
                nombre_pais = form.cleaned_data['nombre_pais'],
                cod_iata_pais = form.cleaned_data['cod_iata_pais'],
            )
            paisx.save()
            return redirect('aaae:nuevoPais')
        else:
             return render(request,'paisCreate.html',{'form':form})
    else:
        form = PaisForm
    return render(request,'paisCreate.html',{'form':form})

def ciudad_create(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if  form.is_valid():
            form.save()
        return redirect ('appCliente: index')
    else:
        form = CiudadForm()
    return render(request,'ciudadCreate.html',{'form':form})

def curso_exito(request):
    return render(request,'exito.html',None)