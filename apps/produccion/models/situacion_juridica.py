from django.db import models

from apps.produccion.models.unidad_produccion import UnidadProduccion

from apps.auxiliares.models.razon_social import RazonSocial
from apps.auxiliares.models.estatus_legal import EstatusLegal

class SituacionJuridica(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT, related_name= 'unidad_juridica')
    estatus_legal = models.ForeignKey(EstatusLegal, on_delete=models.PROTECT)
    razon_social = models.ForeignKey(RazonSocial, on_delete=models.PROTECT, related_name= 'rs_sitacion_juridica')
    duracion = models.CharField(max_length=50)
    convenio = models.CharField(max_length=50)
    telefono = models.IntegerField()
    observacion = models.TextField()

    responsable = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT, related_name='responsable_unidad')

    class Meta:
        managed = True
        db_table = 'produccion\".\"situacion_juridica'
        verbose_name        = 'Situacion Juridica'
        verbose_name_plural = 'Situacion Juridica'

    def __str__(self):
        return f'{self.unidad}-{self.estatus_legal}'