from django.db import models
from django.contrib.auth import get_user_model
from apps.category.models import Category

# Create your models here.
User = get_user_model()

class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Не в наличии')
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )
    title = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='products',
        null=True
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media')
    price = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    stock = models.CharField(choices=STATUS_CHOICES, max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
