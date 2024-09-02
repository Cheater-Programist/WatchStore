from rest_framework.routers import DefaultRouter

from apps.base.views import PostAPI
from apps.users.views import UserAPI
from apps.cart.views import CartViewSet

router = DefaultRouter()
router.register('base', PostAPI, 'api_base')
router.register('users', UserAPI, 'api_users')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = router.urls