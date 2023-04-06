from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from product.filters import CategoryFilter
from product.models import Category
from product.serializers import CategorySerializer


class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
