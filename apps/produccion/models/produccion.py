from django.db import models

class Produccion(models.Model):
    capacidad_instalada = models.FloatField()
    capacidad_operativa = models.FloatField()

    class Meta:
        managed = True
        db_table = 'produccion\".\"produccion'
        verbose_name        = 'Produccion'
        verbose_name_plural = 'Producciones'

    # def __str__(self):
    #     return self.descripcion