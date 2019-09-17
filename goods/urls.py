from django.urls import path, include
from rest_framework.routers import DefaultRouter
from goods import views

router = DefaultRouter()
router.register('goods', views.GoodsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
