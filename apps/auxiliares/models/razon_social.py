from django.db import models
from apps.auxiliares.models.tipo_responsable import TipoResponsable

class RazonSocial(models.Model):
    descripcion = models.CharField("Descripcion", blank=True)
    rif = models.CharField("RIF", max_length=11, blank= True)
    direccion = models.CharField("Dirección", blank=True)
    telefono = models.BigIntegerField("Teléfono")
    fecha_registro = models.DateField("Fecha de Registro", auto_now=False, auto_now_add=False, null= True)
    estatus = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"razon_social'
        verbose_name        = 'Razon Social'
        verbose_name_plural = 'Razones Sociales'

    def __str__(self):
        return self.descripcion