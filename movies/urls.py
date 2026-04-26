from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, CountryViewSet, StreamingPlatformViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'platforms', StreamingPlatformViewSet, basename='platform')

urlpatterns = [
    path('', include(router.urls)),
]