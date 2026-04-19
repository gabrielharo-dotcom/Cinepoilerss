# movies/admin.py
from django.contrib import admin
from .models import Movie, Spoiler

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'created_at')
    search_fields = ('title',)

@admin.register(Spoiler)
class SpoilerAdmin(admin.ModelAdmin):
    list_display = ('movie', 'created_at')
    search_fields = ('movie__title',)