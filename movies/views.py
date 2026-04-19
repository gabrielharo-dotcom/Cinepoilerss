# movies/views.py
from rest_framework import viewsets
from .models import Movie, Spoiler
from .serializers import MovieSerializer, SpoilerSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet proporciona automáticamente las acciones:
    'list', 'create', 'retrieve', 'update' y 'destroy' para las películas.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SpoilerViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los spoilers.
    """
    queryset = Spoiler.objects.all()
    serializer_class = SpoilerSerializer