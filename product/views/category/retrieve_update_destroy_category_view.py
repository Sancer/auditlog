from rest_framework import generics

from product.models import Category
from product.serializers import CategorySerializer


class RetrieveUpdateDestroyCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
