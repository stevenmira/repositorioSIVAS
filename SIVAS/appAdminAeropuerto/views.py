from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from appAdminAeropuerto.forms import *
from appAdminAeropuerto.models import *


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

def ciudad_create(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if  form.is_valid():
            ciudadx = ciudad(
                pais = form.cleaned_data['pais'],
                cod_iata_ciudad = form.cleaned_data['cod_iata_ciudad'],
                nombre_ciudad = form.cleaned_data['nombre_ciudad'],
            )
            form.save()
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

########################
####CRUD EstadoCivil####
########################
class lista_estado(ListView):
    model = estado_civil
    template_name = "estadoCivil/listaEstadoCivil.html"
    paginate_by = 10

def estado_create(request):
    if request.method == 'POST':
        form = EstadoCivilForm(request.POST)
        if  form.is_valid():
            estadox = estado_civil(
                nombre_estado = form.cleaned_data['nombre_estado'],
            )
            estadox.save()
            return redirect('aaae:listaEstado')
        else:
             return render(request,'estadoCivil/estadoCreate.html',{'form':form})
    else:
        form = EstadoCivilForm
    return render(request,'estadoCivil/estadoCreate.html',{'form':form})

class EstadoUpdate(UpdateView):
    model = estado_civil
    form_class = EstadoCivilForm
    template_name = "estadoCivil/estadoUpdate.html"
    success_url = reverse_lazy('aaae:listaEstado')

class EstadoDelete(DeleteView):
    model = estado_civil
    template_name = "estadoCivil/estadoDelete.html"
    success_url = reverse_lazy('aaae:listaEstado')

###################
####CRUD Genero####
###################
class GeneroList(ListView):
    model = genero
    template_name = "genero/listaGenero.html"
    paginate_by = 10

def genero_create(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if  form.is_valid():
            estadox = genero(
                nombre_genero = form.cleaned_data['nombre_genero'],
            )
            estadox.save()
            return redirect('aaae:listaGenero')
        else:
             return render(request,'genero/generoCreate.html',{'form':form})
    else:
        form = GeneroForm
    return render(request,'genero/generoCreate.html',{'form':form})

class GeneroUpdate(UpdateView):
    model = genero
    form_class = GeneroForm
    template_name = "genero/generoUpdate.html"
    success_url = reverse_lazy('aaae:listaGenero')

class GeneroDelete(DeleteView):
    model = genero
    template_name = "genero/generoDelete.html"
    success_url = reverse_lazy('aaae:listaGenero')

###########################
####CRUD Tipo Documento####
###########################
class TipoList(ListView):
    model = tipo_documento
    template_name = "tipoDocumento/listaTipoDocumento.html"
    paginate_by = 10

def tipo_create(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if  form.is_valid():
            estadox = tipo_documento(
                nombre_tipo_documento = form.cleaned_data['nombre_tipo_documento'],
            )
            estadox.save()
            return redirect('aaae:listaTipo')
        else:
             return render(request,'tipoDocumento/tipoDocumentoCreate.html',{'form':form})
    else:
        form = TipoForm
    return render(request,'tipoDocumento/tipoDocumentoCreate.html',{'form':form})

class TipoUpdate(UpdateView):
    model = tipo_documento
    form_class = TipoForm
    template_name = "tipoDocumento/tipoDocumentoUpdate.html"
    success_url = reverse_lazy('aaae:listaTipo')

class TipoDelete(DeleteView):
    model = tipo_documento
    template_name = "tipoDocumento/tipoDocumentoDelete.html"
    success_url = reverse_lazy('aaae:listaTipo')

'''
class ciudad_create(CreateView):
    model = ciudad
    form_class = CiudadForm
    template_name = "ciudad/ciudadCreate.html"
    success_url = reverse_lazy('aaae:listaPais')
'''