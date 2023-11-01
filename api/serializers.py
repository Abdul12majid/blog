from rest_framework import serializers
from my_blog_app.models import Post


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=('title', 'author', 'author_name',)


