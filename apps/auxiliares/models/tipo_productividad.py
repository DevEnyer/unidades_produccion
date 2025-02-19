from django.db import models

class TipoProductividad(models.Model):
    descripcion = models.CharField("Descripcion",blank=True, null=True)
    estatus = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table            = 'auxiliares\".\"tipo_productividad'
        verbose_name        = 'Tipo de Productividad'
        verbose_name_plural = 'Tipos de Productividad'

    def __str__(self):
        return self.descripcion