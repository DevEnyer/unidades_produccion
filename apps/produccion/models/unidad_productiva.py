from django.db import models

from apps.geo.models.estados import Estados
from apps.geo.models.municipios import Municipio
from apps.geo.models.parroquias import Parroquia

from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.auxiliares.models.entes_encomienda import EnteEncomienda
from apps.auxiliares.models.razon_social import RazonSocial

from apps.produccion.models.produccion import Produccion

class UnidadProduccion(models.Model):
    nombre = models.CharField()
    estado = models.ForeignKey(Estados, verbose_name='estado_id', on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, verbose_name='municipio_id', on_delete=models.CASCADE)
    parroquia = models.ForeignKey(Parroquia, verbose_name='parroquia_id', on_delete=models.CASCADE)
    direccion = models.CharField('Dirección')
    tipos_establecimiento = models.ForeignKey(TipoEstablecimiento, verbose_name='tipos_establecimiento_id', on_delete=models.CASCADE)
    descripcion_actividad = models.TextField('Descripción de la actividad')
    razon_social = models.ForeignKey(RazonSocial, verbose_name='razon_social_id', on_delete=models.CASCADE)
    ente_encomienda = models.ForeignKey(EnteEncomienda, verbose_name='ente_encomienda_id', on_delete=models.CASCADE)
    fecha_encomienda = models.DateField(auto_now=False, auto_now_add=False)
    convenio = models.TextField()
    estatus = models.BooleanField(default=True)
    productividad_activa = models.ForeignKey(Produccion, verbose_name='produccion_id', on_delete=models.CASCADE)
    porcentaje_actividad = models.FloatField()
    cantidad_trabajadores = models.IntegerField()
    observaciones = models.TextField()

    class Meta:
        managed = True
        db_table = 'produccion\".\"unidad_produccion'
        verbose_name        = 'Unidad de Producción'
        verbose_name_plural = 'Unidades de Producción'

    # def __str__(self):
    #     return self.descripcion