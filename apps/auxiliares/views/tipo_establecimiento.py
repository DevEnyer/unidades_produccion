from rest_framework                 import generics
from apps.auxiliares.models.tipo_establecimiento import TipoEstablecimiento as Model
from apps.auxiliares.serializers.tipo_establecimiento   import Serializer

class Lista(generics.ListAPIView):
    queryset            = Model.objects.all()
    serializer_class    = Serializer
    paginate_by         = 50
