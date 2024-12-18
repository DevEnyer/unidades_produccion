from rest_framework                     import generics
from apps.geo.models.municipios         import Municipios as Model
from apps.geo.serializers.municipios    import Serializer

class Filtro(generics.ListAPIView):
    serializer_class    = Serializer
    model               = serializer_class.Meta.model
    paginate_by         = 50

    def get_queryset(self):
        estado_me_id          = self.kwargs['estado_me_id']
        queryset        = self.model.objects.filter(estado_me_id = estado_me_id)
        return queryset.order_by('-id')