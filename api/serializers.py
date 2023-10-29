from rest_framework import serializers
from my_blog_app.models import Post, Author


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=('title', 'author', 'author_name',)


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Author
		fields=('id', 'first_name', 'last_name',)
