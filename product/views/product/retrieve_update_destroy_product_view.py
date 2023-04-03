from rest_framework import generics
from rest_framework_simplejwt import authentication

from product.models import Product
from product.serializers import ProductSerializer


class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
