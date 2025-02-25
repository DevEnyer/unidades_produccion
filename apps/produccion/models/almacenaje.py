from django.db import models

from apps.auxiliares.models.tipo_almacenaje import TipoAlmacenaje

from apps.produccion.models.unidad_produccion import UnidadProduccion

class Almacenaje(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT, related_name= 'almacenaje')
    materia_prima = models.FloatField()
    producto_terminado = models.FloatField()
    tipo_almacenaje = models.ForeignKey(TipoAlmacenaje, on_delete=models.PROTECT, related_name= 'almacenaje')

    class Meta:
        managed = True
        db_table = 'produccion\".\"almacenaje'
        verbose_name        = 'Almacenaje'
        verbose_name_plural = 'Almacenajes'

    def __str__(self):
        return self.unidad