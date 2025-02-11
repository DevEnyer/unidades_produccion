from rest_framework                     import generics
from apps.geo.models.parroquias         import Parroquia as Model
from apps.geo.serializers.parroquias    import Serializer

class Filtro(generics.ListAPIView):
    serializer_class    = Serializer
    model               = Model
    paginate_by         = 50

    def get_queryset(self):
        municipio_id = self.kwargs['municipio_id']
        estado_id = self.kwargs['estado_id']
        queryset = self.model.objects.filter(estado_id = estado_id,municipio_id = municipio_id)
        return queryset.order_by('-id')