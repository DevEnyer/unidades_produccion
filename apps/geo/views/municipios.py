from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from apps.geo.models.municipios import Municipio as Model
from apps.geo.serializers.municipios import Serializer

class Filtro(generics.ListAPIView):
    serializer_class = Serializer
    model = Model
    paginate_by = 50

    @extend_schema(
        summary="Filtrar Municipios",
        description="Este endpoint devuelve una lista de municipios que pertenecen a un estado específico, identificado por su `estado_id`.",
        parameters=[
            OpenApiParameter(
                name="estado_id",
                description="ID del estado.",
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
        ],
        responses={
            200: Serializer,
            404: "No se encontraron municipios para el estado especificado.",
        },
    )
    def get(self, request, *args, **kwargs):
        """
        Este método maneja la solicitud GET para filtrar municipios por estado.
        """
        estado_id = self.kwargs.get('estado_id')
        queryset = self.model.objects.filter(estado_id=estado_id).order_by('-id')

        # Serializar los datos
        serializer = self.serializer_class(queryset, many=True)

        # Devolver la respuesta
        return Response(serializer.data)