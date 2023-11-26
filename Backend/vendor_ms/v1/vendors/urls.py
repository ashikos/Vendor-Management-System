from rest_framework.routers import SimpleRouter

from django.urls import path
from . import views 

router = SimpleRouter()


# router.register(r'groups', group.GroupView, basename=Group)



urlpatterns = [
    # path('signup/', views.Signup .as_view()),
]

urlpatterns += router.urls