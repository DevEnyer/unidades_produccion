from rest_framework                 import generics
from apps.auxiliares.models.tipo_productividad import TipoProductividad as Model
from apps.auxiliares.serializers.tipo_productividad   import Serializer

class Lista(generics.ListAPIView):
    queryset            = Model.objects.all()
    serializer_class    = Serializer
    paginate_by         = 50
