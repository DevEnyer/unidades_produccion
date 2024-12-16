from django.urls        import path
from apps.geo.views     import estados

urlpatterns =   [
                    path('estados/lista/',              estados.Lista.as_view(),      name='lista'    ),
                ]