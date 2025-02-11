from rest_framework             import serializers
from apps.geo.models.municipios import Municipio as Model

class Serializer(serializers.ModelSerializer):

    class Meta:
        model   = Model
        #fields  = '__all__'
        exclude = ['id']

        