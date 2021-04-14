from django.db.models.base import Model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from store.models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # def get(self, request):
    #     categories = Category.objects.filter(is_active=True)
    #     serializer = CategorySerializer(categories, many=True)
    #     return Response(serializer.data)
