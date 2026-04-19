# movies/serializers.py
from rest_framework import serializers
from .models import Movie, Spoiler

class SpoilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spoiler
        # Usamos tuplas por convención de inmutabilidad
        fields = ('id', 'movie', 'content', 'created_at')

class MovieSerializer(serializers.ModelSerializer):
    # Esto anidará los spoilers dentro de la película para leerlos de un solo golpe
    spoilers = SpoilerSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'created_at', 'spoilers')