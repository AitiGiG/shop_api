from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=10, required=True, write_only=True)

    class Meta:
        model = User
        fields = 'all'

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs   
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user