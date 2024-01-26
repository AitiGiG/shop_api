from django.db import models
from django.contrib.auth import get_user_model
from apps.category.models import Category

# Create your models here.
User = get_user_model()

class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Нет в наличии'),
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='products')
        
    category = models.ForeignKey(
        Category , 
        related_name = 'products', 
        on_delete=models.SET_NULL, 
        null=True) 
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True, null= True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    