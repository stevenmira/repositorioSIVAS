from django.conf.urls import url, include
from appAdminAeropuerto.views import *

urlpatterns = [
    url(r'^nuevo$',aeropuerto_create,name='aeropuerto_create'),
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

]