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

    #CRUD EstadoCivil
    url(r'^lista-estado$',lista_estado.as_view(), name='listaEstado'),
    url(r'^nuevo-estado$',estado_create, name='nuevoEstado'),
    url(r'^editar-estado/(?P<pk>\d+)/$',EstadoUpdate.as_view(),name='estadoEditar'),
    url(r'^eliminar-estado/(?P<pk>\d+)/$',EstadoDelete.as_view(),name='estadoEliminar'),

    #CRUD Genero
    url(r'^lista-genero$',GeneroList.as_view(), name='listaGenero'),
    url(r'^nuevo-genero$',genero_create, name='nuevoGenero'),
    url(r'^editar-genero/(?P<pk>\d+)/$',GeneroUpdate.as_view(),name='generoEditar'),
    url(r'^eliminar-genero/(?P<pk>\d+)/$',GeneroDelete.as_view(),name='generoEliminar'),

    #CRUD TipoGenero
    url(r'^lista-tipo$',TipoList.as_view(), name='listaTipo'),
    url(r'^nuevo-tipo$',tipo_create, name='nuevoTipo'),
    url(r'^editar-tipo/(?P<pk>\d+)/$',TipoUpdate.as_view(),name='tipoEditar'),
    url(r'^eliminar-tipo/(?P<pk>\d+)/$',TipoDelete.as_view(),name='tipoEliminar'),

    url(r'^lista-gateway/(?P<pk>\w+)/$',GatewayList,name='listaGateway'),
    url(r'^editar-gateway/(?P<pk>\d+)/$',GatewayUpdate.as_view(),name='gatewayEditar'),
    url(r'^nuevo-gateway$',GatewayCreate.as_view(), name='nuevoGateway'),
    url(r'^eliminar-gateway/(?P<pk>\d+)/$',GatewayDelete.as_view(), name='gatewayEliminar'),


    url(r'^lista-cliente$',ClienteList.as_view(), name='listaCliente'),
    url(r'^eliminar-cliente/(?P<pk>\d+)/$',ClienteDelete.as_view(),name='clienteEliminar'),

    #CRUD TipoTargeta
    url(r'^lista-targeta$',TargetaList.as_view(), name='listaTargeta'),
    url(r'^nuevo-targeta$',targeta_create, name='nuevoTargeta'),
    url(r'^editar-targeta/(?P<pk>\d+)/$',TargetaUpdate.as_view(),name='targetaEditar'),
    url(r'^eliminar-targeta/(?P<pk>\d+)/$',TargetaDelete.as_view(),name='targetaEliminar'),


] 