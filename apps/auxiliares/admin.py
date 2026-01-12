from django.contrib import admin
from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento
from apps.auxiliares.models.tipo_productividad import TipoProductividad
from apps.auxiliares.models.tipo_responsable import TipoResponsable
from apps.auxiliares.models.responsable import Responsable
from apps.auxiliares.models.razon_social import RazonSocial
from apps.auxiliares.models.estatus_legal import EstatusLegal

from  django.utils.html 			      import format_html

#admin.site.register(TipoEstablecimiento)
#admin.site.register(TipoProductividad)
#admin.site.register(TipoAlmacenaje)
# admin.site.register(TipoResponsable)
@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):

    def editar(self, obj):
        return format_html('<a class="btn btn-primary btn-sm" href="/admin/auxiliares/responsable/{}/change/"><i class="nav-icon fas fa-eye" title="Ver detalles"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn btn-danger btn-sm" href="/admin/auxiliares/responsable/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    list_display        = ('nombre', 'apellido', 'telefono', 'tipo_responsable', 'editar', 'eliminar')
    #list_filter         = ('motivo',)
    search_fields       = []
    list_display_links  = None
    actions             = None
admin.site.register(RazonSocial)
#admin.site.register(EstatusLegal)

