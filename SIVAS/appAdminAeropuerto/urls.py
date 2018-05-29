from django.conf.urls import url, include
from appAdminAeropuerto.views import *

urlpatterns = [
    url(r'^nuevo$',aeropuerto_create,name='aeropuerto_create'),
    url(r'^nuevo-pais$',pais_create, name='nuevoPais'),
    url(r'^lista-pais$',PaisList.as_view(), name='listaPais'),
    url(r'^nueva-ciudad$',ciudad_create, name='ciudad_create'),

    url(r'^exito$',curso_exito, name='exito'),
]