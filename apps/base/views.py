from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.base.models import Post
from apps.base.serializers import PostSerializer
# Create your views here.

class PostAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer