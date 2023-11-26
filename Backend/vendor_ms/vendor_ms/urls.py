
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('djadmin/', admin.site.urls),

    path("v1/accounts/", include("v1.accounts.urls")),
    path("v1/vendors/", include("v1.vendors.urls"))
    
]
