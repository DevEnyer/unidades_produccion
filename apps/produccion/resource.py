from import_export import resources, fields

from apps.produccion.models.unidad_produccion import UnidadProduccion

class UnidadProduccionResource(resources.ModelResource): # Clase para definir la exportación de datos con Import-Export
    nombre = fields.Field(attribute='nombre', column_name='Nombre')
    estado = fields.Field(attribute='estado__descripcion', column_name='Estado')
    municipio = fields.Field(attribute='municipio__descripcion', column_name='Municipio')
    parroquia = fields.Field(attribute='parroquia__descripcion', column_name='Parroquia')
    direccion = fields.Field(attribute='direccion', column_name='Dirección')
    tipos_establecimiento = fields.Field(attribute='tipos_establecimiento__descripcion', column_name='Tipo establecimiento')
    descripcion_actividad = fields.Field(attribute='descripcion_actividad', column_name='Descripción de la actividad')
    #productividad_activa = fields.Field(attribute='productividad_activa', column_name='Productividad')
    cantidad_trabajadores = fields.Field(attribute='cantidad_trabajadores', column_name='Trabajadores')
    responsables = fields.Field(column_name='Responsables')
    observaciones = fields.Field(attribute='observaciones', column_name='Observaciones')
    class Meta:
        model = UnidadProduccion
        fields = (
            'nombre', 
            'estado', 
            'municipio', 
            'parroquia', 
            'direccion', 
            'tipos_establecimiento', 
            'descripcion_actividad', 
            #'productividad_activa', 
            'cantidad_trabajadores', 
            'responsables', 
            'observaciones'
        )
        export_order = fields
    
    def dehydrate_responsables(self, unidad):
        # Aquí usamos el método que ya creaste inteligentemente en tu modelo
        return unidad.get_responsables()