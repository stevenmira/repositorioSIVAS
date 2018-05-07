from django.db import models

# Create your models here.

class pais(models.Model):
	id_pais = models.AutoField(primary_key=True)
	codigo_pais = models.IntegerField(null=False, blank=False)
	nombre_pais = models.CharField(max_length=30, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'pais'

	def __str__(self):
		return '%s %s %s' % (self.id_pais, self.codigo_pais, self.nombre_pais)

class ciudad(models.Model):
	id_ciudad = models.AutoField(primary_key=True)
	pais = models.ForeignKey(pais, null=False, db_column='id_pais', on_delete=models.CASCADE)
	codigo_ciudad = models.IntegerField(null=False, blank=False)
	nombre_ciudad = models.CharField(max_length=30, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'ciudad'

	def __str__(self):
		return '%s %s %s' % (self.id_ciudad, self.codigo_ciudad, self.nombre_ciudad)

class aeropuerto(models.Model):
	codigo_aeropuerto = models.CharField(primary_key=True, max_length=10)
	ciudad = models.ForeignKey(ciudad, null=False, db_column='id_ciudad', on_delete=models.CASCADE)
	nombre_aeropuerto = models.CharField(max_length=50, null=False, blank=False)
	telefono_aeropuerto = models.CharField(max_length=15, null=False, blank=False)
	nombre_responsable = models.CharField(max_length=50, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'aeropuerto'

	def __str__(self):
		return '%s %s %s %s' % (self.codigo_aeropuerto, self.nombre_aeropuerto, self.telefono_aeropuerto, self.nombre_responsable)

class linea_aerea(models.Model):
	codigo_linea_aerea = models.CharField(primary_key=True, max_length=10)
	pais = models.ForeignKey(pais, null=False, db_column='id_pais', on_delete=models.CASCADE)
	nombre_oficial = models.CharField(max_length=50 ,null=False, blank=False)
	nombre_corto = models.CharField(max_length=30, null=False, blank=False)
	fecha_fundacion = models.DateField(null=False, blank=False)
	nombre_representante = models.CharField(max_length=50, null=False, blank=False)
	direccion_facebook = models.CharField(max_length=30, null=True, blank=True)
	direccion_twitter = models.CharField(max_length=30, null=True, blank=True)
	email_linea_aerea = models.EmailField(max_length=255, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'linea_aerea'

	def __str__(self):
		return '%s %s %s %s %s %s %s %s' % (self.codigo_linea_aerea, self.nombre_oficial, self.nombre_corto, self.fecha_fundacion, self.nombre_representante, self.direccion_facebook, self.direccion_twitter, self.email_linea_aerea)

class detalle_linea_aeropuerto(models.Model):
	id_detalle_linea_aeropuerto = models.AutoField(primary_key=True)
	linea_aerea = models.ForeignKey(linea_aerea, null=False, db_column='codigo_linea_aerea', on_delete=models.CASCADE)
	aeropuerto = models.ForeignKey(aeropuerto, null=False, db_column='codigo_aeropuerto', on_delete=models.CASCADE)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'detalle_linea_aeropuerto'

	def __str__(self):
		return '%s' % (self.id_detalle_linea_aeropuerto)

class tipo_avion(models.Model):
	id_tipo_avion = models.AutoField(primary_key=True)
	nombre_tipo_avion = models.CharField(max_length=30, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'tipo_avion'

	def __str__(self):
		return '%s %s' % (self.id_tipo_avion, self.nombre_tipo_avion)

class avion(models.Model):
	id_avion = models.AutoField(primary_key=True)
	linea_aerea = models.ForeignKey(linea_aerea, null=False, db_column='codigo_linea_aerea', on_delete=models.CASCADE)
	tipo_avion = models.ForeignKey(tipo_avion, null=False, db_column='id_tipo_avion', on_delete=models.CASCADE)
	modelo = models.CharField(max_length=30, null=False, blank=False)
	marca = models.CharField(max_length=20, null=False, blank=False)
	capacidad_asientos = models.IntegerField(null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'avion'

	def __str__(self):
		return '%s %s %s %s' % (self.id_avion, self.modelo, self.marca, self.capacidad_asientos)

class vuelo(models.Model):
	codigo_vuelo = models.CharField(primary_key=True, max_length=15)
	aeropuerto_origen = models.ForeignKey(aeropuerto, null=False, related_name='codigo_aeropuerto_origen', db_column='codigo_aeropuerto_origen', on_delete=models.CASCADE)
	aeropuerto_destino = models.ForeignKey(aeropuerto, null=False, related_name='codigo_aeropuerto_destino', db_column='codigo_aeropuerto_destino', on_delete=models.CASCADE)
	avion = models.ForeignKey(avion, null=False, db_column='id_avion', on_delete=models.CASCADE)
	costo_viaje = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
	milla_recorrida = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
	milla_otorgar = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
	tiempo_de_vuelo = models.DateTimeField()

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'vuelo'

	def __str__(self):
		return '%s %s %s %s %s' % (self.codigo_vuelo, self.costo_viaje, self.milla_recorrida, self.milla_otorgar, self.tiempo_de_vuelo)

class hangar(models.Model):
	id_hangar = models.AutoField(primary_key=True)
	aeropuerto = models.ForeignKey(aeropuerto, null=False, db_column='codigo_aeropuerto', on_delete=models.CASCADE)
	codigo_hangar = models.CharField(max_length=10 ,null=False, blank=False)
	estado_hangar = models.CharField(max_length=15, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'hangar'

	def __str__(self):
		return '%s %s %s' % (self.id_hangar, self.codigo_hangar, self.estado_hangar)

class gateway(models.Model):
	id_gateway = models.AutoField(primary_key=True)
	hangar = models.ForeignKey(hangar, null=False, db_column='id_hangar', on_delete=models.CASCADE)
	codigo_gateway = models.CharField(max_length=10 ,null=False, blank=False)
	estado_gateway = models.CharField(max_length=15, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'gateway'

	def __str__(self):
		return '%s %s %s' % (self.id_gateway, self.codigo_gateway, self.estado_gateway)

class horario(models.Model):
	id_horario = models.AutoField(primary_key=True)
	vuelo = models.ForeignKey(vuelo, null=False, db_column='codigo_vuelo', on_delete=models.CASCADE)
	aeropuerto = models.ForeignKey(aeropuerto, null=False, db_column='codigo_aeropuerto', on_delete=models.CASCADE)
	gateway = models.ForeignKey(gateway, null=False, db_column='id_gateway', on_delete=models.CASCADE)
	hora_salida = models.DateTimeField(null=False, blank=False)
	hora_llegada = models.DateTimeField(null=False, blank=False)
	fecha_registro = models.DateField(null=True, blank=True)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'horario'

	def __str__(self):
		return '%s %s' % (self.hora_salida, self.hora_llegada)

class tipo_cabina(models.Model):
	id_tipo_cabina = models.AutoField(primary_key=True)
	nombre_cabina = models.CharField(max_length=30, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'tipo_cabina'

	def __str__(self):
		return '%s %s' % (self.id_tipo_cabina, self.nombre_cabina)

class asiento(models.Model):
	id_asiento = models.AutoField(primary_key=True)
	avion = models.ForeignKey(avion, null=False, db_column='id_avion', on_delete=models.CASCADE)
	tipo_cabina = models.ForeignKey(tipo_cabina, null=False, db_column='id_tipo_cabina', on_delete=models.CASCADE)
	fila = models.CharField(max_length=1, null=True, blank=True)
	letra = models.CharField(max_length=1, null=True, blank=True)
	estado_asiento = models.CharField(max_length=15, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'asiento'

	def __str__(self):
		return '%s %s %s %s' % (self.id_asiento, self.fila, self.letra, self.estado_asiento)

class tarifa(models.Model):
	id_tarifa = models.AutoField(primary_key=True)
	tipo_cabina = models.ForeignKey(tipo_cabina, null=False, db_column='id_tipo_cabina', on_delete=models.CASCADE)
	vuelo = models.ForeignKey(vuelo, null=False, db_column='codigo_vuelo', on_delete=models.CASCADE)
	precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'tarifa'

	def __str__(self):
		return '%s %s' % (self.id_tarifa, self.precio)

class reservacion(models.Model):
	codigo_reservacion = models.CharField(primary_key=True, max_length=15)
	fecha_salida = models.DateTimeField(null=False, blank=False)
	fecha_regreso = models.DateTimeField()
	numero_maletas = models.IntegerField()
	
	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'reservacion'

	def __str__(self):
		return '%s %s %s %s' % (self.codigo_reservacion, self.fecha_salida, self.fecha_regreso, self.numero_maletas)

class itinerario(models.Model):
	id_itinerario = models.AutoField(primary_key=True)
	reservacion = models.ForeignKey(reservacion, null=False, db_column='codigo_reservacion', on_delete=models.CASCADE)
	vuelo = models.ForeignKey(vuelo, null=False, db_column='codigo_vuelo', on_delete=models.CASCADE)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'itinerario'

	def __str__(self):
		return '%s' % (self.id_itinerario)

class genero(models.Model):
	id_genero = models.AutoField(primary_key=True)
	nombre_genero = models.CharField(max_length=1, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'genero'

	def __str__(self):
		return '%s %s' % (self.id_genero, self.nombre_genero)

class tipo_documento(models.Model):
	id_tipo_documento = models.AutoField(primary_key=True)
	nombre_tipo_documento = models.CharField(max_length=20, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'tipo_documento'

	def __str__(self):
		return '%s %s' % (self.id_tipo_documento, self.nombre_tipo_documento)

class estado_civil(models.Model):
	id_estado_civil = models.AutoField(primary_key=True)
	nombre_estado = models.CharField(max_length=15, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'estado_civil'

	def __str__(self):
		return '%s %s' % (self.id_estado_civil, self.nombre_estado)

class cliente_natural(models.Model):
	numero_documento = models.CharField(primary_key=True, max_length=15)
	genero = models.ForeignKey(genero, null=False, db_column='id_genero', on_delete=models.CASCADE)
	tipo_documento = models.ForeignKey(tipo_documento, null=False, db_column='id_tipo_documento', on_delete=models.CASCADE)
	estado_civil = models.ForeignKey(estado_civil, null=False, db_column='id_estado_civil', on_delete=models.CASCADE)
	fecha_nacimiento = models.DateField(null=True, blank=True)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'cliente_natural'

	def __str__(self):
		return '%s %s' % (self.numero_documento, self.fecha_nacimiento)

class cliente_empresa(models.Model):
	nit = models.CharField(primary_key=True, max_length=20)
	nombre_empresa = models.CharField(max_length=30, null=False, blank=False)
	nic_empresa = models.CharField(max_length=20, null=True, blank=True)
	nombre_contacto = models.CharField(max_length=50, null=True, blank=True)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'cliente_empresa'

	def __str__(self):
		return '%s %s %s %s' % (self.nit, self.nombre_empresa, self.nic_empresa, self.nombre_contacto)

class pasajero(models.Model):
	numero_viajero = models.CharField(primary_key=True, max_length=15)
	cliente_natural = models.ForeignKey(cliente_natural, null=True, db_column='numero_documento')
	cliente_empresa = models.ForeignKey(cliente_empresa, null=True, db_column='nit')
	primer_nombre = models.CharField(max_length=20, null=False, blank=False)
	segundo_nombre = models.CharField(max_length=20, null=True, blank=True)
	tercer_nombre = models.CharField(max_length=20, null=True, blank=True)
	primer_apellido = models.CharField(max_length=20, null=False, blank=False)
	segundo_apellido = models.CharField(max_length=20, null=True, blank=True)
	telefono_fijo = models.CharField(max_length=15, null=True, blank=True)
	telefono_movil = models.CharField(max_length=15, null=True, blank=True)
	email_pasajero = models.EmailField(max_length=255, null=True, blank=True)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'pasajero'

	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s' % (self.numero_viajero, self.primer_apellido, self.segundo_nombre, self.tercer_nombre, self.primer_apellido, self.segundo_apellido, self.telefono_movil, self.telefono_fijo, self.email_pasajero)

class detalle_reservacion(models.Model):
	id_detalle_reservacion = models.AutoField(primary_key=True)
	numero_viajero = models.ForeignKey(pasajero, null=False, db_column='numero_viajero')
	codigo_reservacion = models.ForeignKey(reservacion, null=False, db_column='codigo_reservacion')

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'detalle_reservacion'

	def __str__(self):
		return '%s' % (self.id_detalle_reservacion)

class cliente_adicional(models.Model):
	id_cliente_adicional = models.AutoField(primary_key=True)
	genero = models.ForeignKey(genero, null=False, db_column='id_genero')
	detalle_reservacion = models.ForeignKey(detalle_reservacion, null=False, db_column='id_detalle_reservacion')
	primer_nombre_adicional = models.CharField(max_length=20, null=False, blank=False)
	segundo_nombre_adicional = models.CharField(max_length=20, null=True, blank=True)
	tercer_nombre_adicional = models.CharField(max_length=20, null=True, blank=True)
	primer_apellido_adicional = models.CharField(max_length=20, null=False, blank=False)
	segundo_apellido_adicional = models.CharField(max_length=20, null=True, blank=True)
	fecha_nacimiento_adicional = models.DateField()

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'cliente_adicional'

	def __str__(self):
		return '%s' % (self.id_cliente_adicional)

class equipaje(models.Model):
	id_equipaje = models.AutoField(primary_key=True)
	detalle_reservacion = models.ForeignKey(detalle_reservacion, null=False, db_column='id_detalle_reservacion')
	peso = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'equipaje'

	def __str__(self):
		return '%s %s' % (self.id_equipaje, self.peso)

class tipo_tarjeta(models.Model):
	id_tipo_tarjeta = models.AutoField(primary_key=True)
	nombre_tarjeta = models.CharField(max_length=30, null=False, blank=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'tipo_tarjeta'

	def __str__(self):
		return '%s %s' % (self.id_tipo_tarjeta, self.nombre_tarjeta)

class tarjeta(models.Model):
	id_tarjeta = models.AutoField(primary_key=True)
	tipo_tarjeta = models.ForeignKey(tipo_tarjeta, null=False, db_column='id_tipo_tarjeta')
	pasajero = models.ForeignKey(pasajero, null=False, db_column='numero_viajero')
	numero_tarjeta = models.CharField(max_length=15, null=False, blank=False)
	nombre_tarjeta = models.CharField(max_length=35, null=True, blank=True)
	vencimiento = models.DateField()

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'tarjeta'

	def __str__(self):
		return '%s %s %s %s' % (self.id_tarjeta, self.numero_tarjeta, self.nombre_tarjeta, self.vencimiento)

class pago(models.Model):
	id_pago = models.AutoField(primary_key=True)
	tarjeta = models.ForeignKey(tarjeta, null=False, db_column='id_tarjeta')
	reservacion = models.ForeignKey(reservacion, null=False, db_column='codigo_reservacion')
	cantidad_pago = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
	fecha_pago = models.DateField(null=False, blank=True)
	estado_pago = models.CharField(max_length=15, null=False)

	creado_en = models.DateTimeField(auto_now_add=True)
	creado_por = models.EmailField(verbose_name='Created By', max_length=255, null=True, blank=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	actualizado_por = models.EmailField(verbose_name='Updated By', max_length=255, null=True, blank=True)

	class Meta:
		db_table = 'pago'

	def __str__(self):
		return '%s %s %s %s' % (self.id_pago, self.cantidad_pago, self.fecha_pago, self.estado_pago)
































