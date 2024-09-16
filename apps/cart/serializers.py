from rest_framework import serializers

from apps.cart.models import Cart, CartItem
from apps.base.models import Post

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'price']  # Укажи необходимые поля товара

class CartItemSerializer(serializers.ModelSerializer):
    post = ProductSerializer()  # Вложенный сериализатор для товара
    total_price = serializers.SerializerMethodField()  # Поле для вычисления общей стоимости товара

    class Meta:
        model = CartItem
        fields = ['id', 'post', 'quantity', 'total_price']  # Укажи нужные поля

    def get_total_price(self, obj):
        return obj.quantity * obj.post.price  # Вычисляем общую стоимость

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='cart_items')  # Сериализуем элементы корзины

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']  # Поля корзины