from django.db import models

from apps.auxiliares.models.tipo_almacenaje import TipoAlmacenaje
from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.produccion.models.unidad_produccion import UnidadProduccion

class Almacenaje(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT, related_name= 'almacenaje')
    materia_prima = models.FloatField('Materia Prima (TM)')
    producto_terminado = models.FloatField('Producto Terminado (TM)')
    tipo_almacenaje = models.ForeignKey(TipoEstablecimiento, on_delete=models.PROTECT, related_name= 'almacenaje')

    class Meta:
        managed = True
        db_table = 'produccion\".\"almacenaje'
        verbose_name        = 'Almacenaje'
        verbose_name_plural = 'Almacenaje'

    def __str__(self):
        return str(self.unidad)