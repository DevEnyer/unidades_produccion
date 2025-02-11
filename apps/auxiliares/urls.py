from django.urls import path
from apps.auxiliares.views.tipo_productividad import Lista
from apps.auxiliares.views.tipo_establecimiento import Lista as Lista_TipoEstablecimiento

urlpatterns = [
    path('tipo-productividad/',              Lista.as_view(),      name='lista'),
    path('tipo-establecimiento/', Lista_TipoEstablecimiento.as_view(), name='lista_establecimiento'),
]