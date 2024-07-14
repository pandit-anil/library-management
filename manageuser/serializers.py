from rest_framework import serializers
from .models import User

class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','phone_number','profile','address']

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'error':'UserName already exist'})
        return data