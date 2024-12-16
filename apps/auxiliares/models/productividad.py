from django.db import models

class Productividad(models.Model):
    descripcion = models.CharField('Descripcion', max_length=255)
    estatus = models.BooleanField()

    class Meta:
        managed             = True
        db_table            = 'auxiliares\".\"productividad'
        verbose_name        = 'Tipo de Productividad'
        verbose_name_plural = 'Tipos de Productividad'

    def __str__(self):
        return self.descripcion