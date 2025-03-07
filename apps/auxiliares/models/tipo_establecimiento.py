from django.db import models
from apps.auxiliares.models.tipo_productividad import TipoProductividad

class TipoEstablecimiento(models.Model):
    descripcion = models.CharField("Descripción",blank=True, null=True)
    tipo_productividad = models.ForeignKey(TipoProductividad, on_delete=models.SET_NULL, null=True)
    estatus = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"tipo_establecimiento'
        verbose_name        = 'Tipo de Establecimiento'
        verbose_name_plural = 'Tipos de Establecimientos'

    def __str__(self):
        return f'{self.descripcion} - {self.tipo_productividad}'