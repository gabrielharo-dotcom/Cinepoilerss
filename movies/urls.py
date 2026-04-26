from django.urls import path, include
<<<<<<< HEAD
from movies.views import DirectorViewSet
from rest_framework.routers import DefaultRouter    
from .views import MovieViewSet, GenreViewSet, CountryViewSet 
=======
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, CountryViewSet, StreamingPlatformViewSet
>>>>>>> 51db346459ff35aea07c35f731e21b75eea60b0c

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'countries', CountryViewSet, basename='country')
<<<<<<< HEAD
router.register(r'directors', DirectorViewSet)
=======
router.register(r'platforms', StreamingPlatformViewSet, basename='platform')
>>>>>>> 51db346459ff35aea07c35f731e21b75eea60b0c

urlpatterns = [
    path('', include(router.urls)),
]