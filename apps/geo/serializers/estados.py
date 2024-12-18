from rest_framework             import serializers
from apps.geo.models.estados    import Estados as Model

class Serializer(serializers.ModelSerializer):

    class Meta:
        model   = Model
        fields  = ['id','nombre']