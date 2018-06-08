from django.conf.urls import url, patterns, include
from appAdminVuelo.views2 import *



urlpatterns = [
	#Tipo de Avion
	url(r'^avion/tipo/lista$', TipoAvionList.as_view(), name='listaTipoAvion'),
	url(r'^avion/tipo/nuevo$', TipoAvionCreation.as_view(), name='nuevoTipoAvion'),
	url(r'^avion/tipo/editar/(?P<pk>\d+)$', TipoAvionUpdate.as_view(), name='editarTipoAvion'),

	#Avion
	url(r'^avion/lista/(?P<pk>\w+)/$', AvionList, name='listaAvion'),
	url(r'^avion/nuevo/(?P<pk>\w+)/$', AvionCreation, name='nuevoAvion'),
	url(r'^avion/editar/(?P<pk>\d+)/$', AvionEdit, name='editarAvion'),
	url(r'^avion/ver/(?P<pk>\d+)/$', AvionVer, name='verAvion'),
	url(r'^avion/ver/clases/(?P<pk>\d+)/$', AvionClases, name='clasesAvion'),
	url(r'^avion/ver/asientos/(?P<pk>\d+)/$', AvionCabinas, name='asientosAvion'),

	#Vuelo
	url(r'^lineaAerea/vuelo/lista/(?P<pk>\w+)/$', VueloList, name='listaVuelo'),
	url(r'^lineaAerea/vuelo/nuevo/(?P<pk>\w+)/$', VueloCreation, name='nuevoVuelo'),
	url(r'^lineaAerea/vuelo/editar/(?P<pk>\w+)/$', VueloEdit, name='editarVuelo'),

	#Horario
	url(r'^aerolinea/horarios/(?P<pk>\w+)/$', HorarioList, name='listaHorario'),
]

