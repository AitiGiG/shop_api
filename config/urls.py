from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="SHOP API",

        description="mini service for posting your life",

        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('product/', include('apps.product.urls')),
    path('category/', include('apps.category.urls')),
    path('docs/', schema_view.with_ui('swagger')),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
