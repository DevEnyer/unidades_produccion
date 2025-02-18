from django.db import models
from apps.auxiliares.models.tipo_responsable import TipoResponsable

class RazonSocial(models.Model):
    descripcion = models.CharField("Descripcion", blank=True, null=True)
    rif = models.CharField("RIF",blank=True, null=True)
    direccion = models.CharField("Dirección",blank=True, null=True)
    telefono = models.IntegerField("Teléfono")
    fecha_registro = models.DateField("Fecha de Registro", auto_now=False, auto_now_add=False)
    tipo_responsable_id = models.ForeignKey(TipoResponsable, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"razon_social'
        verbose_name        = 'Razon Social'
        verbose_name_plural = 'Razones Sociales'

    def __str__(self):
        return self.descripcion