from django.db import models
from django.core.validators import RegexValidator
from apps.auxiliares.models.tipo_responsable import TipoResponsable

class Responsable(models.Model):
    nombre = models.CharField("Nombre")
    apellido = models.CharField("Apellido")
    telefono = models.CharField("Teléfono", max_length=2, validators=[RegexValidator(r'^\d+$', 'Solo se permiten números.')], help_text="Duración de contrato")
    tipo_responsable = models.ForeignKey(TipoResponsable, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"responsable'
        verbose_name        = 'Responsable'
        verbose_name_plural = 'Responsables'

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.tipo_responsable})'