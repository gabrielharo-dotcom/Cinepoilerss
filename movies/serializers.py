from rest_framework import serializers
from .models import Movie, Genre, Country 

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)
    
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True,
        required=False,
        allow_null=True,
        label="ID del País"
    )

    class Meta:
        model = Movie
        fields = (
            'id', 
            'title', 
            'description', 
            'release_date', 
            'country', 
            'country_id', 
            'genres', 
            'created_at'
        )