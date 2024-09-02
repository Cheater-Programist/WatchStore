from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated
from .models import Cart, CartItem
from apps.base.models import Post
from .serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ViewSet):
    # Ограничиваем доступ только для авторизованных пользователей
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='add')
    def add_to_cart(self, request):
        post_id = request.data.get('post_id')
        quantity = request.data.get('quantity', 1)

        if not post_id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        post = Post.objects.get(id=post_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, post=post)
        cart_item.quantity += int(quantity)
        cart_item.save()

        return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='remove')
    def remove_from_cart(self, request):
        post_id = request.data.get('post_id')

        if not post_id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, post__id=post_id)
        cart_item.delete()

        return Response({'message': 'Product removed from cart'}, status=status.HTTP_200_OK)
