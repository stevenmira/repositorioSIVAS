from django.conf.urls import url, include
from appAdminAeropuerto.views import *

urlpatterns = [
    url(r'^nuevo-aeropuerto$',aeropuerto_create,name='nuevoAeropuerto'),
    url(r'^lista-aeropuerto$',AeroList.as_view(), name='listaAero'),
    url(r'^editar-aeropuerto/(?P<pk>\w+)/$',AeroUpdate.as_view(),name='aeropuertoEditar'),
    
    url(r'^eliminar-aeropuerto/(?P<pk>\w+)/$',AeroDelete.as_view(),name='aeropuertoEliminar'),
    url(r'^nuevo-pais$',pais_create, name='nuevoPais'),
    url(r'^lista-pais$',PaisList.as_view(), name='listaPais'),
    url(r'^nueva-ciudad$',ciudad_create, name='nuevaCiudad'),
    url(r'^lista-ciudad$',CiudadList.as_view(), name='listaCiudad'),
    url(r'^editar-ciudad/(?P<pk>\d+)/$',CiudadUpdate.as_view(),name='ciudadEditar'),
    url(r'^eliminar-ciudad/(?P<pk>\d+)/$',CiudadDelete.as_view(),name='ciudadEliminar'),
    url(r'^editar-pais/(?P<pk>\d+)/$',PaisUpdate.as_view(),name='paisEditar'),
    url(r'^eliminar-pais/(?P<pk>\d+)/$',PaisDelete.as_view(),name='paisEliminar'),
    url(r'^exito$',curso_exito, name='exito'),
    url(r'^lista-gateway/(?P<pk>\w+)/$',GatewayList,name='listaGateway'),
    url(r'^editar-gateway/(?P<pk>\d+)/$',GatewayUpdate.as_view(),name='gatewayEditar'),
    url(r'^nuevo-gateway$',GatewayCreate.as_view(), name='nuevoGateway'),
    url(r'^eliminar-gateway/(?P<pk>\d+)/$',GatewayDelete.as_view(), name='gatewayEliminar'),



    
    
]
