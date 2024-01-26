from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import Product
# Create your models here.

User = get_user_model()

class Rating(models.Model):
    RATING_CHICES = (
        (1, 'Too Bad'), 
        (2, 'Bad'), 
        (3, 'Normal'), 
        (4, 'Good'), 
        (5, 'Perfect')
        )
    product = models.ForeignKey(Product,related_name='ratings',on_delete=models.CASCADE)
    owner = models.ForeignKey(User,related_name='ratings',on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHICES)
    created_at = models.DateField(auto_now_add=True)

    