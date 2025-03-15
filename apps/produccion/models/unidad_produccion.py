from django.db import models

from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.auxiliares.models.estatus_legal import EstatusLegal
from apps.auxiliares.models.razon_social import RazonSocial
from apps.auxiliares.models.responsable import Responsable

from apps.geo.models.estados import Estados
#from apps.geo.models.municipios import Municipio
#from apps.geo.models.parroquias import Parroquia

from apps.produccion.models.produccion import Produccion

class UnidadProduccion(models.Model):
    nombre = models.CharField()
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT)
    #municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    #parroquia = models.ForeignKey(Parroquia, on_delete=models.PROTECT)
    direccion = models.CharField('Dirección')
    tipos_establecimiento = models.ForeignKey(TipoEstablecimiento, on_delete=models.PROTECT)
    descripcion_actividad = models.TextField('Descripción de la actividad')
    fecha_encomienda = models.DateField(auto_now=False, auto_now_add=False)
    convenio = models.CharField()
    estatus = models.BooleanField(default=True)
    productividad_activa = models.BooleanField(default=True)
    #porcentaje_actividad = models.FloatField()
    cantidad_trabajadores = models.IntegerField()
    observaciones = models.TextField(null=True, blank=True)
    responsables = models.ManyToManyField(
        Responsable,
        through='UnidadResponsable',
        related_name='responsables'
    )

    def get_responsables(self):
        return ", ".join([str(responsable) for responsable in self.responsables.all()])
    
    get_responsables.short_description = 'Responsables'


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
