from django.contrib                     import admin

from django.utils.html 			        import format_html

from apps.geo.models.parroquias         import Parroquias


class AdminParroquias(admin.ModelAdmin):
    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/geo/parroquias/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/geo/parroquias/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_object_permission(self, request, view, obj):
        ...
        return obj.id == request.user.id

    list_display        = ('id','estado_me_id','estado_cne_id','estado_ine_id','municipio_me_id','municipio_cne_id','municipio_ine_id','nombre')
    list_filter         = ['estado_me_id','estado_cne_id','estado_ine_id','municipio_me_id','municipio_cne_id','municipio_ine_id','nombre']
    search_fields       = []
    list_display_links  = None
    actions             = None


admin.site.register(Parroquias, AdminParroquias)