# movies/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SpoilerViewSet, GenreViewSet # CAMBIO: Importar GenreViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'spoilers', SpoilerViewSet, basename='spoiler')
# NUEVO: Registro del endpoint de géneros
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
]