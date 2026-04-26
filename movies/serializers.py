from rest_framework import serializers
from .models import Movie, Genre, Country, StreamingPlatform

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = ('id', 'name', 'url', 'logo_url')

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)
    platforms = StreamingPlatformSerializer(many=True, read_only=True)

    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True,
        required=False,
        allow_null=True,
        label="ID del País"
    )
    platform_ids = serializers.PrimaryKeyRelatedField(
        queryset=StreamingPlatform.objects.all(),
        source='platforms',
        many=True,
        write_only=True,
        required=False,
        label="IDs de Plataformas"
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
            'platforms',
            'platform_ids',
            'created_at'
        )