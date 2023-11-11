from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from my_blog_app.models import Post
from .serializers import PostSerializer, SignupSerializer, LoginSerializer, UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
def home(request):
	#authors = Author.objects.all()
	all_post = Post.objects.all()
	serializer = PostSerializer(all_post, many=True)
	#serializer2 = AuthorSerializer(authors, many=True)
	x =serializer.data
	return Response({'data':serializer.data})

@api_view(['GET'])
def post(request, pk):
	get_post = Post.objects.get(id=pk)
	serializer = PostSerializer(get_post, many=False)
	return Response({'data':serializer.data})

@api_view(['GET', 'POST'])
def make_post(request):
	if request.user.is_authenticated:
		serializer = PostSerializer(data=request.data)
		all_post = Post.objects.all().order_by('-date')
		serialize_post = PostSerializer(all_post, many=True)
		if serializer.is_valid():
			serializer.save(author=request.user)
			return Response({'info':'Post uploaded', 'Posts': serialize_post.data})
		else:
			return Response({'info':"Make your post"})
	else:
		return Response({'info':"Kindly login"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def create_account(request, backend='django.contrib.auth.backends.ModelBackend'):
	serializer = SignupSerializer(data=request.data)
	if serializer.is_valid():
		first_name = request.data['first_name']
		last_name = request.data['last_name']
		email = request.data['email']
		password = request.data['password']
		confirm_password = request.data['confirm_password']

		if password == confirm_password:
			if User.objects.filter(username=first_name).exists():
				return Response({'info':"Username already exists, pick another"})
			elif User.objects.filter(email=email).exists():
				return Response({'info':"Email already exists, pick another"})
			else:
				user = User.objects.create_user(
					username=first_name,
					first_name=first_name,
					last_name=last_name,
					email=email,
					password=password
					)
				user.save()
				login(request, user, backend='django.contrib.auth.backends.ModelBackend')
				return redirect('/view_posts')
		else:
			return Response({'info':"Password mismatch"}, status=status.HTTP_404_NOT_FOUND)

	return Response({'info':"Create account"})


@api_view(['GET', 'POST'])
def login_account(request, backend='django.contrib.auth.backends.ModelBackend'):
	serializer = LoginSerializer(data=request.data)
	if serializer.is_valid():
		email = request.data['email']
		password = request.data['password']
		if User.objects.filter(email=email).exists():
			get_user = User.objects.get(email=email)
			get_user_username = get_user.username
			
			user = authenticate(request, username=get_user_username, password=password)
			if user is not None:
				login(request, user, backend='django.contrib.auth.backends.ModelBackend')
				return redirect('/view_posts')
			else:
				return Response({'info':"Wrong Info Provided. Try again."})
		else:
			return Response({'info':"Username does not exists."})

	return Response({'info':"Login Below"})


@api_view(['GET'])
def user_details(request, pk):
	profile = User.objects.get(id=pk)
	serializer = UserSerializer(profile, many=False)
	return Response({profile.username:serializer.data})


@api_view(['GET'])
def post_details(request, pk):
	about_post = Post.objects.get(id=pk)
	serializer = PostSerializer(about_post, many=False)
	return Response({about_post.author_name:serializer.data})


@api_view(['GET', 'DELETE'])
def delete_post(request, pk):
	try:
		post=Post.objects.get(id=pk)
		post.delete()
		return Response({'info':"Post Deleted"}, status=status.HTTP_400_BAD_REQUEST)
	except Post.DoesNotExist:
		return Response({'info':"Post not found"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def delete_user(request, pk):
	try:
		user=User.objects.get(id=pk)
		post.delete()
		return Response({'info':"User Deleted"}, status=status.HTTP_400_BAD_REQUEST)
	except User.DoesNotExist:
		return Response({'info':"User not found"}, status=status.HTTP_400_BAD_REQUEST)
