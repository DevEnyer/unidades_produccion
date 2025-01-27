from rest_framework             import serializers
from apps.geo.models.parroquias import Parroquias as Model

class Serializer(serializers.ModelSerializer):

    class Meta:
        model   = Model
        fields  = ['id','descripcion']