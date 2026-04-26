# movies/models.py
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Género")
    # ELIMINADO: Se retiró el campo description

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    release_date = models.DateField(verbose_name="Fecha de estreno")
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True, verbose_name="Géneros")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ('-release_date',)

    def __str__(self):
        return self.title


class Spoiler(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='spoilers')
    content = models.TextField(verbose_name="Contenido del Spoiler")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Spoiler"
        verbose_name_plural = "Spoilers"
        ordering = ('-created_at',)

    def __str__(self):
        return f"Spoiler de: {self.movie.title}"