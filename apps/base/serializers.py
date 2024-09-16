from rest_framework import serializers

from apps.base.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'price', 'image', 'description')