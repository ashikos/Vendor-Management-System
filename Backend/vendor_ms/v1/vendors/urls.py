from rest_framework.routers import SimpleRouter

from django.urls import path
from v1.vendors import views
from v1.vendors.models import *


router = SimpleRouter()


router.register(r'', views.VendorView, basename=Vendor)



urlpatterns = [
    # path('signup/', views.Signup .as_view()),
]

urlpatterns += router.urls