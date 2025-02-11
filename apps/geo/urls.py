from django.urls import path
from apps.geo.views.estados import Lista
from apps.geo.views.municipios import Filtro as Filtro_Municipio
from apps.geo.views.parroquias import Filtro 

urlpatterns = [
    path('estados/',              Lista.as_view(),      name='lista'),
    path('municipios/<int:estado_id>', Filtro_Municipio.as_view(), name='filtro_municipio'),
    path('parroquias/<int:estado_id>/<int:municipio_id>', Filtro.as_view(), name='filtro_parroquia')
]