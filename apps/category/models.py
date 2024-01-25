from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'