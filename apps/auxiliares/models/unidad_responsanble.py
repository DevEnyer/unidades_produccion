from django.db import models
from apps.auxiliares.models.responsable import Responsable
from apps.produccion.models.unidad_produccion import UnidadProduccion

class UnidadResponsable(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT)
    responsable = models.ForeignKey(Responsable, on_delete=models.PROTECT)

    class Meta:
        managed = True
        unique_together = ('responsable', 'unidad')
        db_table = 'auxiliares\".\"unidad_responsable'

    def __str__(self):
        return f'{self.unidad} - {self.responsable}'