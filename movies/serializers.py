from rest_framework import serializers
from .models import Director, Movie, Genre, Country 

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            'id',
            'name',
            'bio',
            'birth_date',
            'nationality',
            'is_active'
        ]


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)
    director = DirectorSerializer(read_only=True)

    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True,
        required=False,
        allow_null=True
    )

    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        source='genres',
        many=True,
        write_only=True,
        required=False
    )

    director_id = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(),
        source='director',
        write_only=True,
        required=False,
        allow_null=True
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
            'genre_ids',
            'director',
            'director_id',
            'created_at'
        )
# =========================

















