from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('group', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
