from shop.models import *
from shop.serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.only('id', 'title', 'price')
    serializer_class = ProductListSerializer


class ProductDetailAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
