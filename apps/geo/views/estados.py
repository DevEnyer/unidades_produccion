from rest_framework                 import generics
from apps.geo.models.estados        import Estados as Model
from apps.geo.serializers.estados   import Serializer

class Lista(generics.ListAPIView):
    queryset            = Model.objects.all()
    serializer_class    = Serializer
    paginate_by         = 100
