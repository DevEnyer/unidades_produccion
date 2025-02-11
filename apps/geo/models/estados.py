from django.db import models

class Estados(models.Model):
    descripcion = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo\".\"estados'
        verbose_name        = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.descripcion
