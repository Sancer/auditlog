from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from product.filters import ProductFilter
from product.models import Product
from product.serializers import ProductSerializer


class ListCreateProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
