from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Elastic search test microservice",
        default_version='v1',
        description="An integration with Elastic search test",
        terms_of_service="Internal use only !!!",
        contact=openapi.Contact(email="hosea.mungai@churpy.co"),
        license=openapi.License(name="Internal use only !!!"),
    ),
    public = False,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('data/', include('test_app.urls'))
]
