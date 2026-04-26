# movies/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Spoiler, Genre # CAMBIO: Importar Genre
from .serializers import MovieSerializer, SpoilerSerializer, GenreSerializer # CAMBIO: Importar GenreSerializer

# NUEVO: ViewSet para Géneros
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SpoilerViewSet(viewsets.ModelViewSet):
    queryset = Spoiler.objects.all()
    serializer_class = SpoilerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]