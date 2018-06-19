from django.conf.urls import url, patterns, include
from appAdminVuelo.views import *



urlpatterns = [
	
	#Linea Aerea
	url(r'^linea_list/', linea_list.as_view(), name='linea_list'),
    url(r'^lineaCreate/', lineaCreate, name='lineaCreate'),
    url(r'^lineaUpdate/(?P<id_linea>[\w-]+)/$', lineaUpdate, name='lineaUpdate'),
    url(r'^lineaDelete/(?P<pk>[\w-]+)/$', lineaDelete.as_view(), name='lineaDelete'),
    url(r'^lineaDetail(?P<pk>[\w-]+)/$', lineaDetail, name='lineaDetail'),

	#Tipo de Avion
	url(r'^avion/tipo/lista$', TipoAvionList.as_view(), name='listaTipoAvion'),
	url(r'^avion/tipo/nuevo$', TipoAvionCreation.as_view(), name='nuevoTipoAvion'),
	url(r'^avion/tipo/editar/(?P<pk>\d+)$', TipoAvionUpdate.as_view(), name='editarTipoAvion'),

	#Avion
	url(r'^aerolinea/aviones', avion_linea_list.as_view(), name='avionlinea_list'),
	url(r'^avion/lista/(?P<pk>\w+)/$', AvionList, name='listaAvion'),
	url(r'^avion/nuevo/(?P<pk>\w+)/$', AvionCreation, name='nuevoAvion'),
	url(r'^avion/editar/(?P<pk>\d+)/$', AvionEdit, name='editarAvion'),
	url(r'^avion/ver/(?P<pk>\d+)/$', AvionVer, name='verAvion'),
	url(r'^avion/ver/clases/(?P<pk>\d+)/$', AvionClases, name='clasesAvion'),
	url(r'^avion/ver/asientos/(?P<pk>\d+)/$', AvionCabinas, name='asientosAvion'),

	#Vuelo
	url(r'^aerolinea/vuelos', vuelo_linea_list.as_view(), name='vuelolinea_list'),
	url(r'^lineaAerea/vuelo/lista/(?P<pk>\w+)/$', VueloList, name='listaVuelo'),
	url(r'^lineaAerea/vuelo/nuevo/(?P<pk>\w+)/$', VueloCreation, name='nuevoVuelo'),
	url(r'^lineaAerea/vuelo/editar/(?P<pk>\w+)/$', VueloEdit, name='editarVuelo'),

	#Horario
	url(r'^aerolinea/horarios', horario_linea_list.as_view(), name='horariolinea_list'),
	url(r'^aerolinea/aeropuertos/(?P<pk>\w+)/$', HorarioAeropuertosList, name='listaHorario'),
	url(r'^aerolinea/aeropuerto/horario/(?P<pk>\d+)/$', Horario, name='horario'),
	url(r'^aerolinea/aeropuerto/horario/nuevo/(?P<pk>\d+)/$', HorarioCreation, name='nuevoHorario'),

	#Itinerario
	url(r'^aerolinea/itinerario', itinerario_linea_list.as_view(), name='itinerariolinea_list'),
	url(r'^itinerarios/linea/aerea/(?P<pk>\w+)/$', ItinerarioAerolinea, name='itiAerolinea'),
	url(r'^itinerarios/', ItinerarioList, name='itinerarios'),
	url(r'^itinerario/nuevo/(?P<pk>\w+)/$', ItinerarioCreation, name='itiCreate'),
]




















