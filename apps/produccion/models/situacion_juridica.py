from django.db import models
from django.core.validators import RegexValidator

from apps.produccion.models.unidad_produccion import UnidadProduccion

from apps.auxiliares.models.razon_social import RazonSocial
from apps.auxiliares.models.estatus_legal import EstatusLegal

prefijo = (
    ('0414', ('0414')),
    ('0424', ('0424')),
    ('0416', ('0416')),
    ('0426', ('0426')),
    ('0412', ('0412')),
    ('0212', ('0212'))
)

class SituacionJuridica(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT, related_name= 'unidad_juridica')
    estatus_legal = models.ForeignKey(EstatusLegal, on_delete=models.PROTECT)
    razon_social = models.ForeignKey(RazonSocial, on_delete=models.PROTECT, related_name= 'rs_sitacion_juridica')
    duracion = models.CharField(max_length=50)
    convenio = models.CharField(max_length=50)
    prefijo = models.CharField(choices=prefijo)
    telefono = models.CharField("Teléfono", max_length=7, validators=[RegexValidator(r'^\d+$', 'Solo se permiten números.')], blank=True, null=True)
    observacion = models.TextField(blank= True, null=True)


    #responsable = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT, related_name='responsable_unidad')

    class Meta:
        managed = True
        db_table = 'produccion\".\"situacion_juridica'
        verbose_name        = 'Situación Jurídica'
        verbose_name_plural = 'Situación Jurídica'

    def __str__(self):
        return f'{self.unidad}-{self.estatus_legal}'