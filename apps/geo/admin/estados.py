from django.contrib                     import admin

from import_export                      import resources
from import_export.admin                import ImportExportModelAdmin

from django.utils.html 			        import format_html

from apps.geo.models.estados            import Estados


class AdminEstados(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    def has_object_permission(self, request, view, obj):
        ...
        return obj.id == request.user.id

    list_display        = ('id','descripcion')
    list_filter         = []
    search_fields       = []
    list_display_links  = None
    actions             = None


admin.site.register(Estados, AdminEstados)