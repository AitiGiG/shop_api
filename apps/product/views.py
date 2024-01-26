from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from .serializers import ProductSerializer
from .permissions import IsOwner
from .models import Product
from apps.rating.serializers import RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

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
        if self.request == 'GET':
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [IsOwner(), permissions.IsAuthenticated()]
    
    @action(detail=True , methods=['GET', 'POST', 'PUTCH','PUT', 'DELETE'])
    def rating(self, request, pk):
        product = self.get_object()
        user = request.user
    
        if request.method == 'GET':
            ratings = product.ratings.all()
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data, 200)
        elif request.method == 'POST':
            serializer = RatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=user, product=product)
            return Response(serializer.data, status=201)
        elif request.method in ['PUTCH', 'PUT']:
            if not product.ratings.filter(owner= user).exists():
                return Response('Ты не оставлял рэйтинг на этот продукт', 400)
            rating = product.ratings.get(owner= user)
            serializer = RatingSerializer(rating , data = request.data, partial = True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, 200)

            return Response(serializer.data, status=200)
        elif request.method == 'DELETE':
            rating = product.ratings.get(owner=user)
            rating.delete()
            return Response('Удалено',status=204)