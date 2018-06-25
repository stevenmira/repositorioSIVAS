"""SIVAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appCliente.views import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import logout_then_login
from appCliente.views2 import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),

    url(r'^before$', before, name='before'),
    url(r'^register$', register, name='register'),
    url(r'^registeremp$', register_emp, name='registerempresa'),
    url(r'^ingreso$', ingreso, name='ingreso'),
    url(r'^tarj$', tarjet, name='tarjeta'),
    url(r'^perfil$', login_required(perfil), name='perfil'),
    url(r'^cliente/buscar$',indexBusqueda,name='buscarVuelo'),
    url(r'^cliente/resultado$',busqueda,name='resultado'),
    url(r'^logout$', login_required(logoute), name='logout'),
    url(r'^bienvenido$', bienvenido, name='bienvenido'),
    url(r'^llegada/$', llegada, name='llegada'),
]
