# movies/models.py
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Género")

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ('name',)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del País")

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    release_date = models.DateField(verbose_name="Fecha de estreno")
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True, verbose_name="Géneros")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='movies', verbose_name="País de origen")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ('-release_date',)

    def __str__(self):
        return self.title