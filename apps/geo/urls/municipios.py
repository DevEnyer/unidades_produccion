from django.urls        import path
from apps.geo.views     import municipios

urlpatterns =   [
                    path('municipios/filtro/<int:estado_me_id>/', municipios.Filtro.as_view(),     name='filtro'   ),
                ]