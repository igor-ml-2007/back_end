from django.urls import path
from shop.views import *


urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('product-detail/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('create-order/', CreateOrderAPIView.as_view(), name='create-order'),
    path('category-list/', CategoryListAPIView.as_view(), name='category-list')
]