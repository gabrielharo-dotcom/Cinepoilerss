from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    release_date = models.DateField(verbose_name="Fecha de estreno")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ('-release_date',)

    def __str__(self):
        return self.title