from rest_framework             import serializers
from apps.geo.models.estados    import Estados as Model

class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Model
        fields = '__all__'