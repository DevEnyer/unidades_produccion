from django.db                  import models
from apps.geo.models.estados    import Estados
from apps.geo.models.municipios import Municipios

class Parroquia(models.Model):
    id = models.IntegerField(primary_key=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    descripcion = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo\".\"parroquia'
        verbose_name        = 'Parroquia'
        verbose_name_plural = 'Parroquias'

    def __str__(self):
        return self.descripcion