from rest_framework import serializers
import hashlib

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'age', 'phone',)

    def get_age(self, obj):
        return obj.age
        
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'date_of_birth', 'phone',
                   'password', 'confirm_password')
        
    def validate(self, attrs):
        if len(attrs['password']) < 8:
            raise serializers.ValidationError('Пароль слишком короткий')
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Пароли отличаются")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user