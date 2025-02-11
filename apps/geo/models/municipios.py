from django.db                  import models
from apps.geo.models.estados    import Estados

class Municipio(models.Model):
    estado_id = models.IntegerField()
    municipio_id = models.IntegerField()
    descripcion = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo\".\"municipios'
        verbose_name        = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.descripcion
