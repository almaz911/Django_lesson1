from tabnanny import verbose
from django.db import models

# Create your models here.

class News(models.Model):
    """
    это модель описывает структуру новости в базе данных.
    """

    title = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=150)
    create_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def __str__(self) -> str:
        return f"id:{self.id} {self.title}"






