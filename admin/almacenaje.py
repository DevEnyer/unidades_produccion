from  django.contrib import admin

from apps.produccion.models.almacenaje import Almacenaje

class AdminAlmacenaje(admin.ModelAdmin):
    
     # Accesos directos del lado derecho
    def ver(self, obj):
        return format_html('<a class="btn btn-primary btn-sm" href="/admin/produccion/almacenaje/{}/change/"><i class="nav-icon fas fa-eye" title="Ver detalles"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn btn-danger btn-sm" href="/admin/produccion/almacenaje/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        # if request.user.groups.filter(name='Analista').exists():
        #     return False
        return True

    def has_delete_permission(self, request, obj=None):
        # if request.user.groups.filter(name='Analista').exists():
        #     return False
        return True

  
    list_display        = ('unidad', 'materia_prima', 'producto_terminado','ver','eliminar')
    #list_filter         = ('motivo',)
    search_fields       = []
    list_display_links  = None
    actions             = None

admin.site.register(Almacenaje, AdminAlmacenaje)