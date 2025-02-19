from django.db import models
from apps.auxiliares.models.responsable import Responsable
from apps.produccion.models.unidad_produccion import UnidadProduccion

class UnidadResponsable(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, verbose_name='unidad_id', on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, verbose_name='responsable_id', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"unidad_responsable'

    # def __str__(self):
    #     return self.descripcion