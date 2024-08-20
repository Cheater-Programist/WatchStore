from rest_framework.generics import ListAPIView

from base.models import Post
from base.serializers import PostSerializer
# Create your views here.

class PostAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer