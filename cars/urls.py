from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
