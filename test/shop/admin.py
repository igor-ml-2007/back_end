from django.contrib import admin
from shop.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['created_at']

@admin.register(ToWhom)
class ToWhomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(ProductReason)
class ProductReasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']


@admin.register(ProductToWhom)
class ProductToWhom(admin.ModelAdmin):
    list_display = ['id', 'product']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'feedback']
    list_filter = ['created_at']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    inlines = [OrderItemInline]
