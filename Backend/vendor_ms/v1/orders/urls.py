from rest_framework.routers import SimpleRouter

from v1.orders.models import *
from v1.orders import views 

from django.urls import path


router = SimpleRouter()


router.register(r'', views.OrderView, basename=Order)



urlpatterns = [
    # path('signup/', views.Signup .as_view()),
]

urlpatterns += router.urls