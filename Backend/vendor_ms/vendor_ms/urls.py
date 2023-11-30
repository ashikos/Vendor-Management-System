from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.contrib import admin
from django.urls import path
from django.conf.urls import include

schema_view = get_schema_view(
   openapi.Info(
      title="Vendor Management System V1 API",
      default_version='v1',
   ),
   public=True,
)


urlpatterns = [
    path('djadmin/', admin.site.urls),

    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path("api/accounts/", include("v1.accounts.urls")),
    path("api/vendors/", include("v1.vendors.urls")),
    path("api/purchase_orders/", include("v1.orders.urls"))
    
]
