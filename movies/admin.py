from django.contrib import admin
from .models import Director, Movie, Genre, Country 
from .models import Movie, Genre, Country, StreamingPlatform

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(StreamingPlatform)
class StreamingPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'country', 'created_at')
    search_fields = ('title',)
    filter_horizontal = ('genres',)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'is_active')
    filter_horizontal = ('genres', 'platforms')
