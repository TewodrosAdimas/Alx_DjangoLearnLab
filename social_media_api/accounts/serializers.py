from rest_framework import serializers
from rest_framework.authtoken.models import Token  
from django.contrib.auth import get_user_model  


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
               serializers.CharField()", "get_user_model().objects.create_user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'password']  

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


        Token.objects.create(user=user)

        return user