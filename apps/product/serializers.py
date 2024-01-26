from .models import Product
from rest_framework import serializers
from apps.category.models import Category
from django.db.models import Avg
class ProductSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source = 'owner.id')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['rating'] = instance.ratings.aggregate(Avg('rating'))
        rating = rep['rating']
        rating['rating_count'] = instance.ratings.count()
        return rep 