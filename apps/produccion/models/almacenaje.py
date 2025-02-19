from django.db import models

from apps.produccion.models.unidad_produccion import UnidadProduccion

class Almacenaje(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, verbose_name='unidad_produccion', on_delete=models.CASCADE)
    capacidad_operativa = models.FloatField()

    class Meta:
        managed = True
        db_table = 'produccion\".\"produccion'
        verbose_name        = 'Produccion'
        verbose_name_plural = 'Producciones'

    # def __str__(self):
    #     return self.descripcion