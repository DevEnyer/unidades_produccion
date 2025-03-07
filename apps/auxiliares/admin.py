from django.contrib import admin
from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.auxiliares.models.tipo_productividad import TipoProductividad
from apps.auxiliares.models.tipo_responsable import TipoResponsable
from apps.auxiliares.models.responsable import Responsable
from apps.auxiliares.models.razon_social import RazonSocial
from apps.auxiliares.models.estatus_legal import EstatusLegal

# admin.site.register(TipoEstablecimiento)
# admin.site.register(TipoProductividad)
# admin.site.register(TipoResponsable)
@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    list_display        = ('nombre', 'apellido', 'telefono', 'tipo_responsable')
    #list_filter         = ('motivo',)
    search_fields       = []
    list_display_links  = None
    actions             = None
admin.site.register(RazonSocial)
admin.site.register(EstatusLegal)

