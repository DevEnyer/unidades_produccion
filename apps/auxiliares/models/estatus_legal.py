from django.db import models

class EstatusLegal(models.Model):
    descripcion = models.CharField("Descripcion", blank=True, null=True)
    estatus = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'auxiliares\".\"estatus_legal'
        verbose_name        = 'Estatus Legal'
        verbose_name_plural = 'Estatus Legales'

    def __str__(self):
        return self.descripcion