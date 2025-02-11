from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from apps.geo.models.estados import Estados as Model
from apps.geo.serializers.estados import EstadoSerializer

class Lista(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = EstadoSerializer
    #paginate_by = 100

    @extend_schema(
        summary="Lista de Estados",
        description="Este endpoint devuelve una lista de todos los estados disponibles en el sistema.",
        parameters=[
            """ OpenApiParameter(
                name="search",
                description="Filtra los estados por nombre.",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="page",
                description="Número de página para la paginación.",
                required=False,
                type=int,
            ), """
        ],
        responses={
            200: EstadoSerializer,
            400: "Solicitud inválida",
        },
    )
    def get(self, request, *args, **kwargs):
        """
        Este método maneja la solicitud GET para listar los estados.
        """
        return super().get(request, *args, **kwargs)