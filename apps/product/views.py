from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from .serializers import ProductSerializer
from .permissions import IsOwner
from .models import Product

# Create your views here.
class StandartResultPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandartResultPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.IsAuthenticatedOrReadOnly()]