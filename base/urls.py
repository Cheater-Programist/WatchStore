from rest_framework.routers import DefaultRouter

from base.views import PostAPI
from users.views import UserAPI

router = DefaultRouter()
router.register('base', PostAPI, 'api_base')
router.register('users', UserAPI, 'api_users')

urlpatterns = router.urls