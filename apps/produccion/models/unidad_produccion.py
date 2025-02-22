from django.db import models

from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.auxiliares.models.entes_encomienda import EnteEncomienda
from apps.auxiliares.models.razon_social import RazonSocial
from apps.auxiliares.models.responsable import Responsable

from apps.produccion.models.produccion import Produccion

class UnidadProduccion(models.Model):
    nombre = models.CharField()
    estado = models.IntegerField()
    municipio = models.IntegerField()
    parroquia = models.IntegerField()
    direccion = models.CharField('Dirección')
    tipos_establecimiento = models.ForeignKey(TipoEstablecimiento, on_delete=models.PROTECT)
    descripcion_actividad = models.TextField('Descripción de la actividad')
    razon_social = models.ForeignKey(RazonSocial, related_name='razon_social_unidad' ,on_delete=models.PROTECT)
    ente_encomienda = models.ForeignKey(EnteEncomienda, on_delete=models.PROTECT)
    fecha_encomienda = models.DateField(auto_now=False, auto_now_add=False)
    convenio = models.TextField()
    estatus = models.BooleanField(default=True)
    productividad_activa = models.ForeignKey(Produccion, on_delete=models.PROTECT)
    porcentaje_actividad = models.FloatField()
    cantidad_trabajadores = models.IntegerField()
    observaciones = models.TextField()
    responsables = models.ManyToManyField(
        Responsable,
        through='UnidadResponsable',
        related_name='responsables'
    )

    class Meta:
        managed = True
        db_table = 'produccion\".\"unidad_produccion'
        verbose_name        = 'Unidad de Producción'
        verbose_name_plural = 'Unidades de Producción'

    def __str__(self):
        return self.nombre

class UnidadResponsable(models.Model):
    unidad = models.ForeignKey(UnidadProduccion, on_delete=models.PROTECT)
    responsable = models.ForeignKey(Responsable, on_delete=models.PROTECT)

    class Meta:
        managed = True
        unique_together = ('responsable', 'unidad')
        db_table = 'auxiliares\".\"unidad_responsable'

    def __str__(self):
        return f'{self.unidad} - {self.responsable}'
