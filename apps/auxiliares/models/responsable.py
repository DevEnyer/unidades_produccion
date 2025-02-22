from django.db import models
from apps.auxiliares.models.tipo_responsable import TipoResponsable

class Responsable(models.Model):
    nombre = models.CharField("Nombre")
    apellido = models.CharField("Apellido")
    telefono = models.BigIntegerField("Teléfono")
    tipo_responsable = models.ForeignKey(TipoResponsable, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'produccion\".\"responsable'
        verbose_name        = 'Responsable'
        verbose_name_plural = 'Responsables'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'