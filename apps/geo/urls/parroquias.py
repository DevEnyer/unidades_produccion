from django.urls        import path
from apps.geo.views     import parroquias

urlpatterns =   [
                    path('parroquias/filtro/<int:municipio_me_id>/', parroquias.Filtro.as_view(),     name='filtro'   ),
                ]