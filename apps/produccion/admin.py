from django.contrib import admin
from apps.produccion.models.almacenaje import Almacenaje
from apps.produccion.models.produccion import Produccion
from apps.produccion.models.unidad_produccion import UnidadProduccion
from apps.produccion.models.situacion_juridica import SituacionJuridica

admin.site.register(Almacenaje)
admin.site.register(Produccion)
admin.site.register(UnidadProduccion)
admin.site.register(SituacionJuridica)