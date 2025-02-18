from django.db import models

class TipoResponsable(models.Model):
    descripcion = models.CharField("Descripción",blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"tipo_responsable'
        verbose_name        = 'Tipo de Responsable'
        verbose_name_plural = 'Tipos de Responsables'

    def __str__(self):
        return self.descripcion