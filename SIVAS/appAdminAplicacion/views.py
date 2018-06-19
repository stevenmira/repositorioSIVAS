from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from appAdminVuelo.forms import *
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView

)

from appAdminAplicacion.forms import RegistroForm

from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	return render(request,"inicio/index.html")

class UsuarioList(ListView):
    model = User
    template_name ="usuario/usuario_list.html"
    paginate_by = 10

class RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy("aaap:list_usuario")




