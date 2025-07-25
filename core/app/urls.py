from django.contrib import admin
from django.urls import path, include


# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Beam Test",
        default_version='v1',
        description="Rest API тест",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.product.urls")),
    path('api/', include('core.api.urls')),


    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-swagger-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-swagger-yaml'),

]
