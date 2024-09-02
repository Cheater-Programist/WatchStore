from django.db import models
from django.contrib.auth import get_user_model

from apps.base.models import Post

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="carts_user",
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name="Корзина"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="product_items",
        verbose_name="Товар"
    )
    
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество"
    )

    def __str__(self):
        return f"{self.cart.user.username} || {self.post} || {self.quantity}"
    
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"