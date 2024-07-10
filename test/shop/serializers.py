from rest_framework import serializers
from shop.models import *
from common.serializers import MediaURLSerializer


class ProductToWhomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductToWhom
        fields = ('id', 'who')
        read_only_fields = fields


class ProductReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReason
        fields = ('id', 'reason')
        read_only_fields = fields


class ProductImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ProductImage
        fields = ('image',)
        read_only_fields = fields


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'title')
        read_only_fields = fields


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'feedback')
        read_only_fields = fields


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    product_images = ProductImageSerializer(many=True)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    product_images = ProductImageSerializer(many=True)
    who = ProductToWhomSerializer(many=True)
    reason = ProductReasonSerializer(many=True)
    tags = TagsSerializer(many=True)
    feedback = FeedbackSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'category', 'product_images', 'who', 'reason',
                  'tags', 'feedback', 'title', 'desc')

        read_only_fields = fields


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.ModelSerializer):
    products = serializers.ListSerializer(child=OrderItemSerializer())

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'products')


class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'products_count')

    def get_products_count(self, obj):
        return obj.product_set.count()





