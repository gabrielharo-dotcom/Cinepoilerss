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
    
class Director(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movies"
    )

    director = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movies"
    )

    genres = models.ManyToManyField(Genre, blank=True, related_name="movies")

    def __str__(self):
        return self.title



