from django.contrib                     import admin

from django.utils.html 			        import format_html

from apps.geo.models.parroquias         import Parroquia


class AdminParroquias(admin.ModelAdmin):
    # Accesos directos del lado derecho
    """ def editar(self, obj):
        return format_html('<a class="btn" href="/admin/geo/parroquias/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/geo/parroquias/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id) """

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_object_permission(self, request, view, obj):
        ...
        return obj.id == request.user.id

    list_display        = ('estado_id','municipio_id','parroquia_id','descripcion')
    # list_filter         = ['estado_id','municipio_id','parroquia_id']
    search_fields       = []
    list_display_links  = None
    actions             = None

    list_per_page = 15


admin.site.register(Parroquia, AdminParroquias)