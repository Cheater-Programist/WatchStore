from rest_framework import serializers

from apps.cart.models import Cart, CartItem
from apps.base.models import Post


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    post = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
