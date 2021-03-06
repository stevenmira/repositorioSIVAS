from django.shortcuts import render, redirect, get_object_or_404
from appAdminVuelo.forms import *
from appAdminAplicacion.models import *
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.template import  RequestContext
from django.http import Http404
from django.views.generic import DeleteView, ListView, DetailView
import math

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

class linea_list(ListView):
    model = linea_aerea
    template_name = "lineaAerea/linea_list.html"
    paginate_by = 10


def lineaCreate(request):
    if request.method == 'POST':
        form = LineaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aav:linea_list')
    else:
        form = LineaForm()
        return render(request, 'lineaAerea/linea_create.html', {'form': form})


def lineaUpdate(request, id_linea):
    linea = linea_aerea.objects.get(codigo_linea_aerea=id_linea)
    if request.method == 'GET':
        form = LineaForm(instance=linea)
    else:
        form = LineaForm(request.POST, instance=linea)
        if form.is_valid():
            form.save()
        return redirect('aav:linea_list')
    return render(request, 'lineaAerea/linea_create.html', {'form': form})

class lineaDelete(DeleteView):
    model = linea_aerea
    template_name = "lineaAerea/linea_delete.html"
    success_url = reverse_lazy('aav:linea_list')


def lineaDetail(request, pk):
    try:
        linea_id = linea_aerea.objects.get(codigo_linea_aerea=pk)
    except linea_aerea.DoesNotExist:
        raise Http404("Linea Aerea does not exist")

    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'lineaAerea/linea_detail.html',
        context={'linea': linea_id, }
    )


# Create your views here.

class TipoAvionList(ListView):
    model = tipo_avion
    template_name ="tipoAvion/tipoAvion_list.html"
    paginate_by = 5

class TipoAvionCreation(CreateView):
    model = tipo_avion
    success_url = reverse_lazy('aav:listaTipoAvion')
    template_name ="tipoAvion/tipoAvion_form.html"
    form_class = TipoAvionForm

class TipoAvionUpdate(UpdateView):
    model = tipo_avion
    success_url = reverse_lazy('aav:listaTipoAvion')
    template_name ="tipoAvion/tipoAvion_form.html"
    form_class = TipoAvionForm

class avion_linea_list(ListView):
    model = linea_aerea
    template_name = "avion/linea_list.html"
    paginate_by = 10

def AvionList(request, pk):
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = pk)
    aviones = avion.objects.filter(linea_aerea = lineaAerea).order_by('-id_avion')
    return render(request, 'avion/avion_list.html', {'aviones':aviones, 'lineaAerea':lineaAerea})

def AvionCreation(request,pk):
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = pk)
    tipoAvion = tipo_avion.objects.all()

    if request.method == 'POST':
        
        form = AvionForm(request.POST)
        if form.is_valid():
            avionX = avion(
                linea_aerea = lineaAerea,
                tipo_avion = form.cleaned_data['tipo_avion'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'], 
                capacidad_asientos = form.cleaned_data['capacidad_asientos'],
                estado_avion = 'ACTIVO')
            avionX.save()
            return redirect('aav:listaAvion', pk)
        else:
            return render(request, 'avion/avion_nuevo_form.html',{'form':form,'tipoAvion':tipoAvion, 'pk':pk}, context_instance = RequestContext(request))
    else:
        form = AvionForm
    return render(request, 'avion/avion_nuevo_form.html',{'form':form, 'tipoAvion':tipoAvion, 'pk':pk}, context_instance = RequestContext(request))

def AvionEdit(request, pk):
    avionX = get_object_or_404(avion, pk = pk)
    tipoA = avionX.tipo_avion
    lineaAerea = avionX.linea_aerea
    codigo_linea_aerea = lineaAerea.codigo_linea_aerea
    tipoAvion = tipo_avion.objects.all()

    if request.method == 'POST':
        form = AvionForm(request.POST, instance = avionX)
        if form.is_valid():
            avionX.save()
            return redirect('aav:listaAvion', codigo_linea_aerea)
        else:
            return render(request, 'avion/avion_edit_form.html',{'form':form,'tipoAvion':tipoAvion,'tipoA':tipoA,'codigo_linea_aerea':codigo_linea_aerea}, context_instance = RequestContext(request))
    else:
        form = AvionForm(instance=avionX)
    return render(request, 'avion/avion_edit_form.html',{'form':form,'tipoAvion':tipoAvion, 'tipoA':tipoA,'codigo_linea_aerea':codigo_linea_aerea}, context_instance = RequestContext(request))


def AvionVer(request, pk):
    avionX = get_object_or_404(avion, pk = pk)
    clases = detalle_clase.objects.filter(avion = avionX).order_by('id_detalle_clase')
    return render(request, 'avion/avion_detail.html', {'avionX':avionX, 'clases':clases})

def AvionClases(request, pk):
    avionX = get_object_or_404(avion, pk = pk)
    tipoCabina = tipo_cabina.objects.all().order_by('id_tipo_cabina')
    mensaje = ""

    try:
        clases = detalle_clase.objects.filter(avion = avionX)

        suma = 0
        for clase in clases:
            suma = float(suma) + float(clase.cantidad_asientos)
        suma = int(suma)

        disponible = int(avionX.capacidad_asientos) - suma 
    except Exception:
        suma = ""
        disponible = ""

    if request.method == 'POST':
        form = DetalleClaseForm(request.POST)
        if form.is_valid():
                
            if form.cleaned_data['cantidad_asientos'] <= 0:
                mensaje = "La cantidad de asientos a asignar debe ser mayor a 'CERO'. "
                return render(request, 'avion/avion_cabinas.html',{'form':form,'avionX':avionX, 'tipoCabina':tipoCabina, 'disponible':disponible, 'mensaje':mensaje}, context_instance = RequestContext(request))


            #Descomponemos la cadena para sumar asientos por letra
            cadena = form.cleaned_data['conf_columnas']
            sumaLetra = 0
            for i in cadena:
                if i.isdecimal():
                    sumaLetra = sumaLetra + int(i)

            if sumaLetra <= 0:
                mensaje = "La cantidad de asiento por filas debe ser mayor a 'CERO'. Revise el campo LETRA"
                return render(request, 'avion/avion_cabinas.html',{'form':form,'avionX':avionX, 'tipoCabina':tipoCabina, 'disponible':disponible, 'mensaje':mensaje}, context_instance = RequestContext(request))

            if form.cleaned_data['cantidad_asientos'] > disponible: 
                mensaje = "La cantidad de asientos a asignar excede la cantidad  de asientos disponible en el avión."
                return render(request, 'avion/avion_cabinas.html',{'form':form,'avionX':avionX, 'tipoCabina':tipoCabina, 'disponible':disponible, 'mensaje':mensaje}, context_instance = RequestContext(request))

            detalle_claseX = detalle_clase(
                avion = avionX,
                tipo_cabina = form.cleaned_data['tipo_cabina'],
                cantidad_asientos = form.cleaned_data['cantidad_asientos'],
                conf_columnas = form.cleaned_data['conf_columnas'], 
                conf_filas = form.cleaned_data['conf_filas'],
                estado_clase = 'ACTIVO')
            detalle_claseX.save()

            m = form.cleaned_data['cantidad_asientos']  #75
            n = sumaLetra                               #9
            filas = math.ceil(m/n)

            fila=1
            cont=1
            while(cont <= m):                                               # de 1 hasta 75
                letra = 1                                                   # se reinicia a 1
                for i in range(sumaLetra):                                  # de 0 hasta 8
                    if cont > m:                                            # cont = 76
                        return redirect('aav:verAvion', avionX.id_avion)
                    else: 
                        asientoX = asiento()                                        
                        asientoX.detalle_clase = detalle_claseX
                        asientoX.fila = fila
                        asientoX.columna = chr(64 + letra)                  # A
                        asientoX.estado_asiento = 'DISPONIBLE'
                        asientoX.save()
                        cont = cont + 1                                         # cont = 2
                    letra = letra + 1                                       # letra = 2
                fila = fila + 1                                             # fila = 2
        else:
            return render(request, 'avion/avion_cabinas.html',{'form':form,'avionX':avionX, 'tipoCabina':tipoCabina, 'disponible':disponible}, context_instance = RequestContext(request))
    else:
        form = DetalleClaseForm
    return render(request, 'avion/avion_cabinas.html',{'form':form, 'avionX':avionX, 'tipoCabina':tipoCabina, 'disponible':disponible}, context_instance = RequestContext(request))


def AvionCabinas(request, pk):
    avionX = get_object_or_404(avion, pk = pk)
    detalle_clases = detalle_clase.objects.filter(avion = avionX).order_by('id_detalle_clase')
    longitud = len(detalle_clases)

    lista = []

    for i in range(longitud):
        pkp = detalle_clases[i].id_detalle_clase
        detalle_claseX = detalle_clase.objects.get(id_detalle_clase = pkp)
        asientosClase = asiento.objects.filter(detalle_clase = detalle_claseX).order_by('id_asiento')
        
        j = 1
        var1 = 'inicio'
        lista.append(var1)

        for asientoX in asientosClase:
            if asientoX.fila == j:
                x = asientoX.columna
                y = asientoX.fila
                z = x + str(y) 
                #lista.append(z)
                lista.append(asientoX)
            else:
                var2 = 'fin'
                lista.append(var2)
                x = asientoX.columna
                y = asientoX.fila
                z = x + str(y) 
                #lista.append(z)
                lista.append(asientoX)
                j = j + 1     
    

    return render(request, 'avion/avion_asientos.html', {'lista':lista, 'detalle_clases':detalle_clases, 'avionX':avionX})

class vuelo_linea_list(ListView):
    model = linea_aerea
    template_name = "vuelo/linea_list.html"
    paginate_by = 10


def VueloList(request, pk):
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = pk)
    vuelos = vuelo.objects.filter(linea_aerea = lineaAerea).order_by('codigo_vuelo')
    return render(request, 'vuelo/vuelo_list.html', {'lineaAerea':lineaAerea, 'vuelos':vuelos})

def VueloCreation(request,pk):
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = pk)
    aeropuertos = aeropuerto.objects.all()
    lineas = linea_aerea.objects.all()
    mensaje = ""

    vuelos = vuelo.objects.filter(linea_aerea = lineaAerea)
    cant = len(vuelos)
    cadena = lineaAerea.nombre_corto

    if cant == 0:
        codigo = cadena[0] + cadena[1] + str(0) + str(1)
    else:
        cant = cant + 1
        codigo = cadena[0] + cadena[1] + str(0) + str(cant)


    if request.method == 'POST':
        
        form = VueloForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['aeropuerto_origen'] == form.cleaned_data['aeropuerto_destino']:
                mensaje = "El aeropuerto Origen debe ser diferente al aeropuerto de Destino"
                return render(request, 'vuelo/vuelo_new_form.html',{'form':form,'aeropuertos':aeropuertos, 'pk':pk,
                'lineas':lineas, 'lineaAerea':lineaAerea, 'codigo':codigo, 'mensaje':mensaje}, context_instance = RequestContext(request))

            vueloX = vuelo(
                codigo_vuelo = form.cleaned_data['codigo_vuelo'],
                linea_aerea = form.cleaned_data['linea_aerea'],
                aeropuerto_origen = form.cleaned_data['aeropuerto_origen'],
                aeropuerto_destino = form.cleaned_data['aeropuerto_destino'],
                costo_viaje = form.cleaned_data['costo_viaje'],
                milla_recorrida = form.cleaned_data['milla_recorrida'],
                milla_otorgar = form.cleaned_data['milla_otorgar'], 
                tiempo_de_vuelo = form.cleaned_data['tiempo_de_vuelo'],
                estado_vuelo = 'PROGRAMADO')
            vueloX.save()
            return redirect('aav:listaVuelo', pk)
        else:
            return render(request, 'vuelo/vuelo_new_form.html',{'form':form,'aeropuertos':aeropuertos, 'pk':pk,
                'lineas':lineas, 'lineaAerea':lineaAerea, 'codigo':codigo}, context_instance = RequestContext(request))
    else:
        form = VueloForm
    return render(request, 'vuelo/vuelo_new_form.html',{'form':form,'aeropuertos':aeropuertos, 'pk':pk,
        'lineas':lineas, 'lineaAerea':lineaAerea, 'codigo':codigo}, context_instance = RequestContext(request))

def VueloEdit(request, pk):
    vueloX = get_object_or_404(vuelo, pk = pk)
    codigo_linea_a = vueloX.linea_aerea.codigo_linea_aerea

    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = codigo_linea_a)
    aeropuertos = aeropuerto.objects.all()
    lineas = linea_aerea.objects.all()
    mensaje = ""

    if request.method == 'POST':
        form = VueloForm(request.POST, instance = vueloX)
        if form.is_valid():
            if form.cleaned_data['aeropuerto_origen'] == form.cleaned_data['aeropuerto_destino']:
                mensaje = "El aeropuerto Origen debe ser diferente al aeropuerto de Destino"

                return render(request, 'vuelo/vuelo_edit_form.html',{'form':form,'aeropuertos':aeropuertos, 'codigo_linea_a':codigo_linea_a,
                'lineas':lineas, 'lineaAerea':lineaAerea, 'mensaje':mensaje}, context_instance = RequestContext(request))

            vueloX.save()
            return redirect('aav:listaVuelo', codigo_linea_a)
        else:
            return render(request, 'vuelo/vuelo_edit_form.html',{'form':form,'aeropuertos':aeropuertos, 'codigo_linea_a':codigo_linea_a,
                'lineas':lineas, 'lineaAerea':lineaAerea}, context_instance = RequestContext(request))
    else:
        form = VueloForm(instance=vueloX)
    return render(request, 'vuelo/vuelo_edit_form.html',{'form':form,'aeropuertos':aeropuertos, 'codigo_linea_a':codigo_linea_a,
        'lineas':lineas, 'lineaAerea':lineaAerea}, context_instance = RequestContext(request))


class horario_linea_list(ListView):
    model = linea_aerea
    template_name = "horario/linea_list.html"
    paginate_by = 10

def HorarioAeropuertosList(request, pk):
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = pk)
    detalles = detalle_linea_aeropuerto.objects.filter(linea_aerea = lineaAerea)
    return render(request, 'horario/aeropuertos_list.html', {'lineaAerea':lineaAerea, 'detalles':detalles})

def Horario(request, pk):
    detalle = detalle_linea_aeropuerto.objects.get(id_detalle_linea_aeropuerto = pk)
    horarios = horario.objects.filter(detalle_linea_aeropuerto = detalle).order_by('hora_salida')
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = detalle.linea_aerea.codigo_linea_aerea)
    aero = aeropuerto.objects.get(codigo_aeropuerto = detalle.aeropuerto.codigo_aeropuerto)
    return render(request, 'horario/horario.html', {'lineaAerea':lineaAerea, 'detalle':detalle, 'horarios':horarios, 'aero':aero})

def HorarioCreation(request, pk):
    pk = pk
    return render(request, 'horario/nuevoHorario.html', {'pk':pk})

class itinerario_linea_list(ListView):
    model = linea_aerea
    template_name = "itinerario/linea_list.html"
    paginate_by = 10

def ItinerarioAerolinea(request, pk):
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = pk)
    itinerarios = itinerario.objects.filter(linea_aerea = lineaAerea)

    cont =len(itinerarios)

    diccionario={}

    for i in range(cont):
        pkp = itinerarios[i].id_itinerario
        iti = itinerario.objects.get(id_itinerario = pkp)
        detalles = detalle_itinerario.objects.filter(itinerario = iti)
        
        diccionario[iti]=[detalles]


    return render(request, 'itinerario/itis_linea.html', {'lineaAerea':lineaAerea, 'itinerarios':itinerarios, 'diccionario':diccionario})

def ItinerarioList(request):
    itinerarios = itinerario.objects.all()
    cont =len(itinerarios)

    diccionario={}

    for i in range(cont):
        pkp = itinerarios[i].id_itinerario
        iti = itinerario.objects.get(id_itinerario = pkp)
        detalles = detalle_itinerario.objects.filter(itinerario = iti)
        
        diccionario[iti]=[detalles]

    return render(request, 'itinerario/itinerarios.html', {'diccionario':diccionario})

def ItinerarioCreation(request, pk):
    lineaAerea = linea_aerea.objects.get(codigo_linea_aerea = pk)
    aeropuertos = detalle_linea_aeropuerto.objects.filter(linea_aerea=lineaAerea)
    lineas = linea_aerea.objects.all()
    vuelos = vuelo.objects.filter(linea_aerea = lineaAerea)
    horarios = horario.objects.filter(vuelo__linea_aerea = lineaAerea).order_by('id_horario')

    if request.method == 'POST':
        form = ItinerarioForm(request.POST)

        if form.is_valid():
            return redirect('aav:itinerariolinea_list')
        else:
            return render(request, 'itinerario/iti_nuevo_form.html', {'form':form,'aeropuertos':aeropuertos,
                'lineaAerea':lineaAerea, 'lineas': lineas, 'horarios': horarios}, 
                context_instance = RequestContext(request))
    else:
        form = ItinerarioForm
    return render(request, 'itinerario/iti_nuevo_form.html', {'form':form,'aeropuertos':aeropuertos, 
        'lineaAerea':lineaAerea, 'lineas': lineas, 'horarios': horarios}, 
        context_instance = RequestContext(request))




