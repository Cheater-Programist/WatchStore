from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.serializers import UserSerializer, UserRegisterSerializer
from users.permissions import UserPermission
from users.models import User

# Create your views here.
class UserAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method in ('DELETE', 'PUT', 'PATCH'):
            return (UserPermission(), )
        return (AllowAny(), )
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)