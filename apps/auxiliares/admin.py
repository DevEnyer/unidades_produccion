from django.contrib import admin
from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.auxiliares.models.tipo_productividad import TipoProductividad
from apps.auxiliares.models.tipo_responsable import TipoResponsable
from apps.auxiliares.models.responsable import Responsable
from apps.auxiliares.models.razon_social import RazonSocial
from apps.auxiliares.models.entes_encomienda import EnteEncomienda

admin.site.register(TipoEstablecimiento)
admin.site.register(TipoProductividad)
admin.site.register(TipoResponsable)
admin.site.register(Responsable)
admin.site.register(RazonSocial)
admin.site.register(EnteEncomienda)

