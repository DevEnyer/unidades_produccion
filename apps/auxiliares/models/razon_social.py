from django.db import models
from django.core.validators import RegexValidator
from apps.auxiliares.models.tipo_responsable import TipoResponsable

class RazonSocial(models.Model):
    descripcion = models.CharField("Descripción")
    rif = models.CharField("RIF", max_length=11)
    direccion = models.CharField("Dirección")
    telefono = models.CharField("Teléfono", max_length=11, validators=[RegexValidator(r'^\d+$', 'Solo se permiten números.')])
    fecha_registro = models.DateField("Fecha de Registro", auto_now=False, auto_now_add=False, null= True)
    estatus = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"razon_social'
        verbose_name        = 'Razon Social'
        verbose_name_plural = 'Razones Sociales'

    def __str__(self):
        return self.descripcion