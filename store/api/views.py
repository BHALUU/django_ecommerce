from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Category
from .serializers import CategorySerializer


class CategoryView(APIView):

    def get(self, request):
        categories = Category.objects.filter(is_active=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer)
