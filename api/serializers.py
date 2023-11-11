from rest_framework import serializers
from my_blog_app.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=('id', 'title', 'author', 'author_name', 'write_up',)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('id', 'first_name', 'last_name', 'email', 'username',)


class SignupSerializer(serializers.Serializer):
	first_name=serializers.CharField()
	last_name=serializers.CharField()
	email=serializers.EmailField()
	password=serializers.CharField()
	confirm_password=serializers.CharField()


class LoginSerializer(serializers.Serializer):
	email=serializers.EmailField()
	password=serializers.CharField()