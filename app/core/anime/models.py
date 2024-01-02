"""Models for anime app"""
from typing import Any
import dataclasses
from django.db import models
from django.utils import timezone

# Create your models here.
class Anime(models.Model):
    """Anime model"""
    title = models.CharField(
        max_length=255,verbose_name='Title'
    )
    description = models.TextField(
        null=True,verbose_name="Description"
    )
    picture = models.ImageField(
        upload_to='static/animes/%Y/%m/%d',
        null=True,blank=True,
        verbose_name="Picture",
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self) -> str:
        return f"{self.title}"

    @dataclasses.dataclass
    class Meta:
        """info for model"""
        verbose_name = "Anime"
        verbose_name_plural = "Anime"
        db_table = "Anime"
        app_label = 'anime'
        ordering = ['id']
