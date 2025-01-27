from django.db                  import models
from apps.geo.models.estados    import Estados

class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    descripcion = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo\".\"municipio'
        verbose_name        = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.descripcion
