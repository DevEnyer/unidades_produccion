from django.db                  import models
from apps.geo.models.estados    import Estados
from apps.geo.models.municipios import Municipio

class Parroquia(models.Model):
    estado_id = models.IntegerField()
    municipio_id = models.IntegerField()
    parroquia_id = models.IntegerField()
    descripcion = models.CharField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'geo\".\"parroquias'
        verbose_name        = 'Parroquia'
        verbose_name_plural = 'Parroquias'

    def __str__(self):
        return self.descripcion