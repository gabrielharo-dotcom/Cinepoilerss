# movies/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SpoilerViewSet

# El router construye las URLs estándar para APIs REST
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'spoilers', SpoilerViewSet, basename='spoiler')

urlpatterns = [
    path('', include(router.urls)),
]