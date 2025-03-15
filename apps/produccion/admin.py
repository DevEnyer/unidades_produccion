from django import forms
from django.core.validators import RegexValidator
from django.contrib import admin
from django.utils.html import format_html

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from apps.produccion.models.almacenaje import Almacenaje
from apps.produccion.models.produccion import Produccion
from apps.produccion.models.unidad_produccion import UnidadProduccion, UnidadResponsable
from apps.produccion.models.situacion_juridica import SituacionJuridica

class UnidadProduccionResource(resources.ModelResource):
    estado = fields.Field(attribute='estado__descripcion', column_name='Estado')
    tipos_establecimiento = fields.Field(attribute='tipos_establecimiento__descripcion', column_name='Tipo establecimiento')
    responsables = fields.Field(column_name='Responsables')
    class Meta:
        model = UnidadProduccion

class AdminUnidadResponsableInline(admin.TabularInline):
    model = UnidadResponsable
    extra = 0

@admin.register(UnidadProduccion)
class UnidadProduccionAdmin(ExportActionModelAdmin):
    inlines = [AdminUnidadResponsableInline,]

    resource_class = UnidadProduccionResource

    def ver(self, obj):
        return format_html('<a class="btn btn-primary btn-sm" href="/admin/produccion/unidadproduccion/{}/change/"><i class="nav-icon fas fa-eye" title="Ver detalles"></i></a>', obj.id)

    def has_change_permission(self, request, obj=None):
        # if request.user.groups.filter(name='Analista').exists():
        #     return False
        return True

    list_display        = ('nombre','estado','tipos_establecimiento', 'get_responsables', 'ver')
    #list_filter         = ('motivo',)
    search_fields       = []
    list_display_links  = None
    actions             = None


class AlmacenajeResource(resources.ModelResource):
    unidad = fields.Field(attribute='unidad__nombre')
    tipo_almacenaje = fields.Field(attribute='tipo_almacenaje__descripcion')
    class Meta:
        model = Almacenaje

@admin.register(Almacenaje)
class AlmacenajeAdmin(ExportActionModelAdmin):

    resource_class = AlmacenajeResource

    def ver(self, obj):
        return format_html('<a class="btn btn-primary btn-sm" href="/admin/produccion/almacenaje/{}/change/"><i class="nav-icon fas fa-eye" title="Ver detalles"></i></a>', obj.id)

    list_display = ('unidad', 'materia_prima', 'producto_terminado')
    #search_fields = ('nombre', 'email')
    #list_filter = ('activo',)

#admin.site.register(Almacenaje)
#admin.site.register(Produccion)

# admin.site.register(UnidadProduccion)


#admin.site.register(SituacionJuridica)
class SituacionJuridicaResource(resources.ModelResource):
    unidad = fields.Field(attribute='unidad__nombre')
    estatus_legal = fields.Field(attribute='estatus_legal__descripcion')
    razon_social = fields.Field(attribute='razon_social__descripcion')
    class Meta:
        model = SituacionJuridica

@admin.register(SituacionJuridica)

class SituacionJuridicaAdmin(ExportActionModelAdmin):

    resource_class = SituacionJuridicaResource

    list_display = ('razon_social', 'estatus_legal', 'observacion')
    fieldsets = (
        (None, {
            'fields': ('unidad', 'estatus_legal', 'razon_social', 'duracion', 'convenio', ('prefijo', 'telefono'), 'observacion'),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['prefijo'].label = 'Teléfono'  # Cambiar "Prefijo" por "Teléfono"
        form.base_fields['telefono'].label = ''  # Eliminar la etiqueta "Teléfono"
        return form
