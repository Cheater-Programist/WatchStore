from django.urls import path
from base.views import PostAPI

urlpatterns = [
    path('', PostAPI.as_view(), name="api_posts"),
]  