from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from my_blog_app.models import Post, Author
from .serializers import PostSerializer, AuthorSerializer

# Create your views here.
@api_view(['GET'])
def home(request):
	authors = Author.objects.all()
	all_post = Post.objects.all()
	serializer = PostSerializer(all_post, many=True)
	serializer2 = AuthorSerializer(authors, many=True)
	x =serializer.data
	return Response({'data':serializer.data})

@api_view(['GET'])
def post(request, pk):
	get_post = Post.objects.get(id=pk)
	serializer = PostSerializer(get_post, many=False)
	return Response({'data':serializer.data})

