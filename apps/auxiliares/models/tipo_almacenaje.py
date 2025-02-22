from django.db import models

class TipoAlmacenaje(models.Model):
    descripcion = models.CharField("Descripción", blank=True, null=True)
    estatus = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'produccion\".\"tipo_almacenaje'
        verbose_name        = 'Tipo Almacenaje'
        verbose_name_plural = 'Tipos Almacenajes'

    def __str__(self):
        return self.descripcion