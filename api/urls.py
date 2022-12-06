"""parts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator


class PublicAPISchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = '/api/'
        return schema

schema_view = get_schema_view(
    openapi.Info(
      title="Parts Unlimited API",
      default_version='v1',
      description="",
      contact=openapi.Contact(email="ggallohernandez@gmail.com"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    url='http://localhost' if settings.APP_ENV == 'development' else None,
    generator_class=PublicAPISchemeGenerator
)

from parts.views import api_root

urlpatterns = [
    re_path(r'^openapi(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('admin/', admin.site.urls),
    path('authenticate/', views.obtain_auth_token, name='authenticate'),
    path('', include('parts.urls')),
]
