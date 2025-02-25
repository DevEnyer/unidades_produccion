from django.contrib import admin
from apps.produccion.models.almacenaje import Almacenaje
from apps.produccion.models.produccion import Produccion
from apps.produccion.models.unidad_produccion import UnidadProduccion
from apps.produccion.models.situacion_juridica import SituacionJuridica

@admin.register(Almacenaje)
class AlmacenajeAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'materia_prima', 'producto_terminado')
    #search_fields = ('nombre', 'email')
    #list_filter = ('activo',)

#admin.site.register(Almacenaje)
admin.site.register(Produccion)

# admin.site.register(UnidadProduccion)
@admin.register(UnidadProduccion)
class UnidadProduccionAdmin(admin.ModelAdmin):
    list_display        = ('nombre','estado','municipio','parroquia','tipos_establecimiento','razon_social','ente_encomienda')
    #list_filter         = ('motivo',)
    search_fields       = []
    list_display_links  = None
    actions             = None

    class Media:
        js  =   ('js/filtro.js',) 

admin.site.register(SituacionJuridica)