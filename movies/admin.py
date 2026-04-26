# movies/admin.py
from django.contrib import admin
from .models import Movie, Spoiler, Genre # CAMBIO: Importar Genre

@admin.register(Genre)
# NUEVO: Registro de Género
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'created_at')
    search_fields = ('title',)
    # NUEVO: Facilita la selección de géneros en una lista doble
    filter_horizontal = ('genres',)

@admin.register(Spoiler)
class SpoilerAdmin(admin.ModelAdmin):
    list_display = ('movie', 'created_at')
    search_fields = ('movie__title',)