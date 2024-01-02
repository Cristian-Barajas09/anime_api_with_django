"""modelo de los capitulos de los animes"""
import dataclasses
from typing import Any
from django.db import models
from django.utils import timezone
from core.anime.models import Anime

# Create your models here.
class Chapter(models.Model):
    """representa los capitulos de los animes"""
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    duration = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    picture = models.ImageField(
        upload_to='static/chapter/%Y/%m/%d',
        null=True,blank=True,
        verbose_name="Picture",
    )
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='chapters')
    anime_chapter = models.ManyToOneRel(anime, to=Anime, field_name='anime_chapter')

    def __str__(self):
        return f"{self.name} - {self.anime.title}"

    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
        """elimina el registro de la base de datos"""
        self.deleted_at = timezone.now()
        self.save()

    @dataclasses.dataclass
    class Meta:
        """informacion del modelo en la base de datos"""
        db_table = 'chapters'
        ordering = ['id']
        verbose_name = 'chapter'
        verbose_name_plural = 'chapters'
