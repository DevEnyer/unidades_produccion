from django.contrib                     import admin

from import_export                      import resources
from import_export.admin                import ImportExportModelAdmin

from django.utils.html 			        import format_html

from apps.geo.models.municipios         import Municipios


class AdminMunicipios(admin.ModelAdmin):
    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/geo/municipios/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/geo/minicipios/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    def has_object_permission(self, request, view, obj):
        ...
        return obj.id == request.user.id

    list_display        = ('id','estado_me_id','estado_cne_id','estado_ine_id','nombre','capital')
    list_filter         = ['estado_me_id','estado_cne_id','estado_ine_id']
    search_fields       = []
    list_display_links  = None
    actions             = None


admin.site.register(Municipios, AdminMunicipios)