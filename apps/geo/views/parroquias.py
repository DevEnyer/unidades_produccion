from rest_framework                     import generics
from apps.geo.models.parroquias         import Parroquias as Model
from apps.geo.serializers.parroquias    import Serializer


class Filtro(generics.ListAPIView):
    serializer_class    = Serializer
    model               = serializer_class.Meta.model
    paginate_by         = 50

    def get_queryset(self):
        municipio_me_id  = self.kwargs['municipio_me_id']
        queryset        = self.model.objects.filter(municipio_me_id = municipio_me_id)
        return queryset.order_by('-id')