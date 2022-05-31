from dataclasses import field
import email
from pyexpat import model
from rest_framework import serializers
from account.models import User

# Create user register serializer.
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email','name','tc','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    #validating password and confirm password while registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    

# Create user login serializer.
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']



#user profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','name']
