from django.shortcuts import render
from appAdminAeropuerto.models import *
from appAdminAeropuerto.forms import *

# Create your views here.

def index(request):
	return render(request,"cliente/index.html")

def register(request):
	gene=genero.objects.all()
	tidoc=tipo_documento.objects.all()
	esta=estado_civil.objects.all()
	if request.method == 'POST':
		nam1=request.POST['primer_nombre']
		nam2=request.POST['segundo_nombre']
		apell1=request.POST['primer_apellido']
		apell2=request.POST['segundo_apellido']
		numedoc=request.POST['numero_documento']
		telefijo=request.POST['telefono_fijo']
		telemovi=request.POST['telefono_movil']
		email=request.POST['email_pasajero']
		pas=request.POST['psw']
		gen=request.POST['genero']
		tip=request.POST['tipo']
		est=request.POST['estado']
		fech=request.POST['fecha']
		print(pas)
		
		gener = genero.objects.get(id_genero=gen)
		tipo_document = tipo_documento.objects.get(id_tipo_documento=tip)
		estado_civi = estado_civil.objects.get(id_estado_civil=est)
		cliente = cliente_natural.objects.create(numero_documento=numedoc,genero=gener,tipo_documento=tipo_document,estado_civil=estado_civi,fecha_nacimiento=fech)
		pasajero.objects.create(numero_viajero=numedoc,cliente_natural=cliente,primer_nombre=nam1,segundo_nombre=nam2,primer_apellido=apell1,segundo_apellido=apell2,telefono_fijo=telefijo,telefono_movil=telemovi,email_pasajero=email)
		return render(request, "cliente/congratulation.html")
	context={
		'genero':gene,
		'tipodoc':tidoc,
		'estado':esta,
	}
	print(context)
	return render(request,"cliente/register.html",context)

def register_emp(request):
	if request.method == 'POST':
		nam1=request.POST['primer_nombre']
		nam2=request.POST['segundo_nombre']
		apell1=request.POST['primer_apellido']
		apell2=request.POST['segundo_apellido']
		nomemp=request.POST['nombre_empresa']
		numedoc=request.POST['numero_documento']
		nomcon=request.POST['nombre_contacto']
		nic=request.POST['nic_empresa']
		telefijo=request.POST['telefono_fijo']
		telemovi=request.POST['telefono_movil']
		email=request.POST['email_pasajero']
		pas=request.POST['psw']
		print(pas)
		
		cliente = cliente_empresa.objects.create(nit=numedoc,nombre_empresa=nomemp,nic_empresa=nic,nombre_contacto=nomcon)
		pasajero.objects.create(numero_viajero=numedoc,cliente_empresa=cliente,primer_nombre=nam1,segundo_nombre=nam2,primer_apellido=apell1,segundo_apellido=apell2,telefono_fijo=telefijo,telefono_movil=telemovi,email_pasajero=email)
		return render(request, "cliente/congratulation.html")

	return render(request,"cliente/registeremp.html")

def before(request):
	return render(request,"cliente/before.html")

def ingreso(request):
	return render(request, "cliente/ingreso.html")