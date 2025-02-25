from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from apps.produccion.models.unidad_produccion import UnidadProduccion, UnidadResponsable

from apps.auxiliares.models.responsable         import Responsable

from apps.geo.models.estados                    import Estados
from apps.geo.models.municipios                 import Municipio
from apps.geo.models.parroquias                 import Parroquia

class UnidadProduccionForm(forms.ModelForm):
    class Meta:
        model = UnidadProduccion
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(UnidadProduccionForm, self).__init__(*args, **kwargs)

        try:
            self.initial['estado'] = kwargs['instance'].estados.id
            estado_lista = [('', '---------')] + [(columna.id, columna.descripcion) for columna in Estados.objects.all()]
        except:
            estado_lista = [('', '---------')]
        

        # try:
        #     self.initial['municipio'] = kwargs['instance'].municipio.id
        #     lista_municipios = [(columna.municipio_id, columna.descripcion) for columna in Municipio.objects.filter(estado_id = kwargs['instance'].estado.id)]
        # except:
        #     lista_municipios = [('', '---------')]

        # try:
        #     self.initial['parroquia'] = kwargs['instance'].parroquia.id
        #     lista_parroquias = [(columna.id, columna.descripcion) for columna in Parroquias.objects.filter(municipio = kwargs['instance'].municipio)]
        # except:
        #     lista_parroquias = [('', '---------')]

        
        # self.fields['estado'].widget = forms.Select(
        #     attrs={
        #         'id':       'estado',
        #         'onchange': 'getMunicipio(this.value)',
        #         'style':    'width:200px'
        #     },
        #     choices=estado_lista,
        # )
        # self.fields['municipio'].widget = forms.Select(
        #     attrs={
        #         'id':       'municipio',
        #         'onchange': 'getParroquia(this.value)',
        #         'style':    'width:200px'
        #     },
        #     choices=lista_municipios
        # )
        # self.fields['parroquia'].widget = forms.Select(
        #     attrs={
        #         'id':       'parroquia',
        #         'onchange': 'getcomunidad(this.value)',
        #         'style':    'width:200px'
        #     },
        #     choices=lista_parroquias
        # )