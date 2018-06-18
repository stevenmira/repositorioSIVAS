# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-06-17 15:26
# Generated by Django 1.9.9 on 2018-06-17 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aeropuerto',
            fields=[
                ('codigo_aeropuerto', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_aeropuerto', models.CharField(max_length=50)),
                ('telefono_aeropuerto', models.CharField(max_length=15)),
                ('nombre_responsable', models.CharField(max_length=50)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'aeropuerto',
            },
        ),
        migrations.CreateModel(
            name='asiento',
            fields=[
                ('id_asiento', models.AutoField(primary_key=True, serialize=False)),
                ('fila', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('columna', models.CharField(blank=True, max_length=10, null=True)),
                ('estado_asiento', models.CharField(max_length=15)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'asiento',
            },
        ),
        migrations.CreateModel(
            name='avion',
            fields=[
                ('id_avion', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=20)),
                ('capacidad_asientos', models.IntegerField()),
                ('estado_avion', models.CharField(blank=True, max_length=15, null=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'avion',
            },
        ),
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_ciudad', models.IntegerField()),
                ('cod_iata_ciudad', models.CharField(max_length=3)),
                ('nombre_ciudad', models.CharField(max_length=30)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'ciudad',
            },
        ),
        migrations.CreateModel(
            name='cliente_adicional',
            fields=[
                ('id_cliente_adicional', models.AutoField(primary_key=True, serialize=False)),
                ('primer_nombre_adicional', models.CharField(max_length=20)),
                ('segundo_nombre_adicional', models.CharField(blank=True, max_length=20, null=True)),
                ('tercer_nombre_adicional', models.CharField(blank=True, max_length=20, null=True)),
                ('primer_apellido_adicional', models.CharField(max_length=20)),
                ('segundo_apellido_adicional', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_nacimiento_adicional', models.DateField()),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'cliente_adicional',
            },
        ),
        migrations.CreateModel(
            name='cliente_empresa',
            fields=[
                ('nit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=30)),
                ('nic_empresa', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre_contacto', models.CharField(blank=True, max_length=50, null=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'cliente_empresa',
            },
        ),
        migrations.CreateModel(
            name='cliente_natural',
            fields=[
                ('numero_documento', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'cliente_natural',
            },
        ),
        migrations.CreateModel(
            name='detalle_clase',
            fields=[
                ('id_detalle_clase', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_asientos', models.IntegerField()),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('conf_columnas', models.CharField(blank=True, max_length=10, null=True)),
                ('conf_filas', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('estado_clase', models.CharField(blank=True, max_length=15, null=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('avion', models.ForeignKey(db_column='id_avion', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.avion')),
            ],
            options={
                'db_table': 'detalle_clase',
            },
        ),
        migrations.CreateModel(
            name='detalle_itinerario',
            fields=[
                ('id_detalle_itinerario', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_det_iti', models.DateField()),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('avion', models.ForeignKey(db_column='id_avion', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.avion')),
            ],
            options={
                'db_table': 'detalle_itinerario',
            },
        ),
        migrations.CreateModel(
            name='detalle_linea_aeropuerto',
            fields=[
                ('id_detalle_linea_aeropuerto', models.AutoField(primary_key=True, serialize=False)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('aeropuerto', models.ForeignKey(db_column='codigo_aeropuerto', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.aeropuerto')),
            ],
            options={
                'db_table': 'detalle_linea_aeropuerto',
            },
        ),
        migrations.CreateModel(
            name='detalle_reservacion',
            fields=[
                ('id_detalle_reservacion', models.AutoField(primary_key=True, serialize=False)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'detalle_reservacion',
            },
        ),
        migrations.CreateModel(
            name='detalle_viaje',
            fields=[
                ('id_detalle_viaje', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_viaje', models.DateTimeField()),
                ('bin_tipo', models.CharField(max_length=6)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'detalle_viaje',
            },
        ),
        migrations.CreateModel(
            name='equipaje',
            fields=[
                ('id_equipaje', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('detalle_reservacion', models.ForeignKey(db_column='id_detalle_reservacion', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.detalle_reservacion')),
            ],
            options={
                'db_table': 'equipaje',
            },
        ),
        migrations.CreateModel(
            name='estado_civil',
            fields=[
                ('id_estado_civil', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=15)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'estado_civil',
            },
        ),
        migrations.CreateModel(
            name='gateway',
            fields=[
                ('id_gateway', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_gateway', models.CharField(max_length=10)),
                ('estado_gateway', models.CharField(max_length=15)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('aeropuerto', models.ForeignKey(db_column='codigo_aeropuerto', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.aeropuerto')),
            ],
            options={
                'db_table': 'gateway',
            },
        ),
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=1)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'genero',
            },
        ),
        migrations.CreateModel(
            name='hangar',
            fields=[
                ('id_hangar', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_hangar', models.CharField(max_length=10)),
                ('estado_hangar', models.CharField(max_length=15)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('aeropuerto', models.ForeignKey(db_column='codigo_aeropuerto', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.aeropuerto')),
            ],
            options={
                'db_table': 'hangar',
            },
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id_horario', models.AutoField(primary_key=True, serialize=False)),
                ('hora_salida', models.DateTimeField()),
                ('hora_llegada', models.DateTimeField()),
                ('fecha_registro', models.DateField(blank=True, null=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('aeropuerto', models.ForeignKey(db_column='codigo_aeropuerto', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.aeropuerto')),
                ('gateway', models.ForeignKey(db_column='id_gateway', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.gateway')),
            ],
            options={
                'db_table': 'horario',
            },
        ),
        migrations.CreateModel(
            name='itinerario',
            fields=[
                ('id_itinerario', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_itinerario', models.DateTimeField()),
                ('monto_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado_itinerario', models.CharField(max_length=15)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('aeropuert_destino', models.ForeignKey(db_column='codigo_aeropuert_destino', on_delete=django.db.models.deletion.CASCADE, related_name='codigo_aeropuert_destino', to='appAdminAplicacion.aeropuerto')),
                ('aeropuert_origen', models.ForeignKey(db_column='codigo_aeropuert_origen', on_delete=django.db.models.deletion.CASCADE, related_name='codigo_aeropuert_origen', to='appAdminAplicacion.aeropuerto')),
            ],
            options={
                'db_table': 'itinerario',
            },
        ),
        migrations.CreateModel(
            name='linea_aerea',
            fields=[
                ('codigo_linea_aerea', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_oficial', models.CharField(max_length=50)),
                ('nombre_corto', models.CharField(max_length=30)),
                ('fecha_fundacion', models.DateField()),
                ('nombre_representante', models.CharField(max_length=50)),
                ('direccion_facebook', models.CharField(blank=True, max_length=30, null=True)),
                ('direccion_twitter', models.CharField(blank=True, max_length=30, null=True)),
                ('email_linea_aerea', models.EmailField(max_length=255)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'linea_aerea',
            },
        ),
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField(blank=True)),
                ('estado_pago', models.CharField(max_length=15)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'pago',
            },
        ),
        migrations.CreateModel(
            name='pais',
            fields=[
                ('id_pais', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_pais', models.IntegerField()),
                ('nombre_pais', models.CharField(max_length=30)),
                ('cod_iata_pais', models.CharField(max_length=2)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='pasajero',
            fields=[
                ('numero_viajero', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('tercer_nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono_fijo', models.CharField(blank=True, max_length=15, null=True)),
                ('telefono_movil', models.CharField(blank=True, max_length=15, null=True)),
                ('email_pasajero', models.EmailField(blank=True, max_length=255, null=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('cliente_empresa', models.ForeignKey(db_column='nit', null=True, on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.cliente_empresa')),
                ('cliente_natural', models.ForeignKey(db_column='numero_documento', null=True, on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.cliente_natural')),
            ],
            options={
                'db_table': 'pasajero',
            },
        ),
        migrations.CreateModel(
            name='reservacion',
            fields=[
                ('codigo_reservacion', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('fecha_salida', models.DateTimeField()),
                ('fecha_regreso', models.DateTimeField()),
                ('numero_maletas', models.IntegerField()),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'reservacion',
            },
        ),
        migrations.CreateModel(
            name='tarifa',
            fields=[
                ('id_tarifa', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('detalle_clase', models.ForeignKey(db_column='id_detalle_clase', null=True, on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.detalle_clase')),
            ],
            options={
                'db_table': 'tarifa',
            },
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('id_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('numero_tarjeta', models.CharField(max_length=15)),
                ('nombre_tarjeta', models.CharField(blank=True, max_length=35, null=True)),
                ('vencimiento', models.DateField()),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('pasajero', models.ForeignKey(db_column='numero_viajero', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.pasajero')),
            ],
            options={
                'db_table': 'tarjeta',
            },
        ),
        migrations.CreateModel(
            name='tipo_avion',
            fields=[
                ('id_tipo_avion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_avion', models.CharField(max_length=30)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'tipo_avion',
            },
        ),
        migrations.CreateModel(
            name='tipo_cabina',
            fields=[
                ('id_tipo_cabina', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cabina', models.CharField(max_length=30)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'tipo_cabina',
            },
        ),
        migrations.CreateModel(
            name='tipo_documento',
            fields=[
                ('id_tipo_documento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_documento', models.CharField(max_length=20)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'tipo_documento',
            },
        ),
        migrations.CreateModel(
            name='tipo_reserva',
            fields=[
                ('id_tipo_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_reserva', models.CharField(max_length=30)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'tipo_reserva',
            },
        ),
        migrations.CreateModel(
            name='tipo_tarjeta',
            fields=[
                ('id_tipo_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tarjeta', models.CharField(max_length=30)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'tipo_tarjeta',
            },
        ),
        migrations.CreateModel(
            name='vuelo',
            fields=[
                ('codigo_vuelo', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('costo_viaje', models.DecimalField(decimal_places=2, max_digits=10)),
                ('milla_recorrida', models.DecimalField(decimal_places=2, max_digits=10)),
                ('milla_otorgar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tiempo_de_vuelo', models.TimeField()),
                ('estado_vuelo', models.CharField(blank=True, max_length=15, null=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('actualizado_por', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Updated By')),
                ('aeropuerto_destino', models.ForeignKey(db_column='codigo_aeropuerto_destino', on_delete=django.db.models.deletion.CASCADE, related_name='codigo_aeropuerto_destino', to='appAdminAplicacion.aeropuerto')),
                ('aeropuerto_origen', models.ForeignKey(db_column='codigo_aeropuerto_origen', on_delete=django.db.models.deletion.CASCADE, related_name='codigo_aeropuerto_origen', to='appAdminAplicacion.aeropuerto')),
                ('linea_aerea', models.ForeignKey(db_column='codigo_linea_aerea', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.linea_aerea')),
            ],
            options={
                'db_table': 'vuelo',
            },
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='tipo_tarjeta',
            field=models.ForeignKey(db_column='id_tipo_tarjeta', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.tipo_tarjeta'),
        ),
        migrations.AddField(
            model_name='tarifa',
            name='vuelo',
            field=models.ForeignKey(db_column='codigo_vuelo', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.vuelo'),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='tipo_reserva',
            field=models.ForeignKey(db_column='id_tipo_reserva', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.tipo_reserva'),
        ),
        migrations.AddField(
            model_name='pago',
            name='reservacion',
            field=models.ForeignKey(db_column='codigo_reservacion', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.reservacion'),
        ),
        migrations.AddField(
            model_name='pago',
            name='tarjeta',
            field=models.ForeignKey(db_column='id_tarjeta', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.tarjeta'),
        ),
        migrations.AddField(
            model_name='linea_aerea',
            name='pais',
            field=models.ForeignKey(db_column='id_pais', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.pais'),
        ),
        migrations.AddField(
            model_name='horario',
            name='vuelo',
            field=models.ForeignKey(db_column='codigo_vuelo', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.vuelo'),
        ),
        migrations.AddField(
            model_name='detalle_viaje',
            name='itinerario',
            field=models.ForeignKey(db_column='id_itinerario', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.itinerario'),
        ),
        migrations.AddField(
            model_name='detalle_viaje',
            name='reservacion',
            field=models.ForeignKey(db_column='codigo_reservacion', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.reservacion'),
        ),
        migrations.AddField(
            model_name='detalle_reservacion',
            name='codigo_reservacion',
            field=models.ForeignKey(db_column='codigo_reservacion', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.reservacion'),
        ),
        migrations.AddField(
            model_name='detalle_reservacion',
            name='numero_viajero',
            field=models.ForeignKey(db_column='numero_viajero', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.pasajero'),
        ),
        migrations.AddField(
            model_name='detalle_linea_aeropuerto',
            name='linea_aerea',
            field=models.ForeignKey(db_column='codigo_linea_aerea', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.linea_aerea'),
        ),
        migrations.AddField(
            model_name='detalle_itinerario',
            name='horario',
            field=models.ForeignKey(db_column='id_horario', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.horario'),
        ),
        migrations.AddField(
            model_name='detalle_itinerario',
            name='itinerario',
            field=models.ForeignKey(db_column='id_itinerario', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.itinerario'),
        ),
        migrations.AddField(
            model_name='detalle_itinerario',
            name='vuelo',
            field=models.ForeignKey(db_column='codigo_vuelo', null=True, on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.vuelo'),
        ),
        migrations.AddField(
            model_name='detalle_clase',
            name='tipo_cabina',
            field=models.ForeignKey(db_column='id_tipo_cabina', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.tipo_cabina'),
        ),
        migrations.AddField(
            model_name='cliente_natural',
            name='estado_civil',
            field=models.ForeignKey(db_column='id_estado_civil', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.estado_civil'),
        ),
        migrations.AddField(
            model_name='cliente_natural',
            name='genero',
            field=models.ForeignKey(db_column='id_genero', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.genero'),
        ),
        migrations.AddField(
            model_name='cliente_natural',
            name='tipo_documento',
            field=models.ForeignKey(db_column='id_tipo_documento', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.tipo_documento'),
        ),
        migrations.AddField(
            model_name='cliente_adicional',
            name='detalle_reservacion',
            field=models.ForeignKey(db_column='id_detalle_reservacion', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.detalle_reservacion'),
        ),
        migrations.AddField(
            model_name='cliente_adicional',
            name='genero',
            field=models.ForeignKey(db_column='id_genero', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.genero'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(db_column='id_pais', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.pais'),
        ),
        migrations.AddField(
            model_name='avion',
            name='linea_aerea',
            field=models.ForeignKey(blank=True, db_column='codigo_linea_aerea', null=True, on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.linea_aerea'),
        ),
        migrations.AddField(
            model_name='avion',
            name='tipo_avion',
            field=models.ForeignKey(blank=True, db_column='id_tipo_avion', null=True, on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.tipo_avion'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='detalle_clase',
            field=models.ForeignKey(db_column='id_detalle_clase', null=True, on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.detalle_clase'),
        ),
        migrations.AddField(
            model_name='aeropuerto',
            name='ciudad',
            field=models.ForeignKey(db_column='id_ciudad', on_delete=django.db.models.deletion.CASCADE, to='appAdminAplicacion.ciudad'),
        ),
    ]
