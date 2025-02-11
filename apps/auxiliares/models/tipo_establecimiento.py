from django.db import models

class TipoEstablecimiento(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(blank=True, null=True)
    estatus = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auxiliares\".\"tipo_establecimiento'
        verbose_name        = 'Tipo de Establecimiento'
        verbose_name_plural = 'Tipos de Establecimientos'

    def __str__(self):
        return self.descripcion