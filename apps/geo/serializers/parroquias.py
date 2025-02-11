from rest_framework             import serializers
from apps.geo.models.parroquias import Parroquia as Model

class Serializer(serializers.ModelSerializer):

    class Meta:
        model   = Model
        #fields  = '__all__'
        exclude = ['id', 'parroquia_id']