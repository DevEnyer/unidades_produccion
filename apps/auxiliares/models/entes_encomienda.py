from django.db import models

class EnteEncomienda(models.Model):
    descripcion = models.CharField("Descripcion", blank=True, null=True)
    estatus = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"ente_encomienda'
        verbose_name        = 'Ente Encomienda'
        verbose_name_plural = 'Entes Encomiendas'

    def __str__(self):
        return self.descripcion