from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer
from rest_framework import permissions

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]