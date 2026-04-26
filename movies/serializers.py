# movies/serializers.py
from rest_framework import serializers
from .models import Movie, Spoiler, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        # CAMBIO: Se eliminó 'description' de la tupla de campos
        fields = ('id', 'name')

class SpoilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spoiler
        fields = ('id', 'movie', 'content', 'created_at')

class MovieSerializer(serializers.ModelSerializer):
    spoilers = SpoilerSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'created_at', 'genres', 'spoilers')