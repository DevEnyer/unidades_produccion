from django.contrib import admin
from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.auxiliares.models.tipo_productividad import TipoProductividad

admin.site.register(TipoEstablecimiento)
admin.site.register(TipoProductividad)

