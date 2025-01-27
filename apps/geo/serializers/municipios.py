from rest_framework             import serializers
from apps.geo.models.municipios import Municipios as Model

class Serializer(serializers.ModelSerializer):

    class Meta:
        model   = Model
        fields  = ['id','descripcion']