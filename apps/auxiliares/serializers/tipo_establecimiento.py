from rest_framework             import serializers
from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento  as Model

class Serializer(serializers.ModelSerializer):

    class Meta:
        model   = Model
        fields  = ['id','descripcion']