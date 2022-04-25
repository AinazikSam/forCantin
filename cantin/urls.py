from django.urls import path, include
from rest_framework.routers import DefaultRouter
from SuperB.views import *
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Authentication API',
        default_version='v1',
        description='Test Description',
    ),
    public=True
)
router = DefaultRouter()
router.register('students', StudentsViewSet)
router.register('products', ProductsViewSet)

urlpatterns = [
    path('home', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('signin.urls')),
]
