from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PostsForm
from django.contrib import messages
from .models import Post, Favorite_Book
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required(login_url='login-user')
def home(request):
	return render(request, "html_files/index.html", {})
	
def create_account(request):
	if request.method == 'POST':
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = first_name
		password_1 = request.POST['password1']
		password_2 = request.POST['password2']
		if password_1 == password_2:
			if User.objects.filter(email=email).exists():
				a = User.objects.filter(email=email).exists()
				return render(request, 'html_files/register_user.html', {'first_name':first_name, 'last_name':last_name, 'email':email, 'a':a})
			elif User.objects.filter(username=username).exists():
				messages.request(request, ('Username Already Exists, pick another.'))
				return render(request, 'html_files/register_user.html', {'first_name':first_name, 'last_name':last_name, 'email':email})
			else:
				user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password_1)
				login(request, user)
				book_id = Post.objects.get(id=1)
				request.user.favorite_book.name_of_book.add(book_id)

				messages.success(request, ('Welcome.'))
				return redirect('view-posts')
		else:
			messages.success(request, ('Password do not match.'))
			return render(request, 'html_files/register_user.html', {'first_name':first_name, 'last_name':last_name, 'email':email})

	return render(request, 'html_files/register_user.html', {})

def login_user(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		if User.objects.filter(email=email).exists():
			get_user = User.objects.get(email=email)
			get_username = get_user.username
			user=authenticate(request, username=get_username, password=password)
			if user is not None:
				login(request, user)
				return redirect('view-posts')
			else:
				x = 'Wrong details'
				return render(request, 'html_files/login_user.html', {'x':x})
		else:
			a = 'User does not exists'
			return render(request, 'html_files/login_user.html', {'a':a})
	return render(request, 'html_files/login_user.html', {})


@login_required(login_url='login-user')
def view_author(request, author_id):
	author = Author.objects.get(pk=author_id)
	return render(request, 'html_files/view_author.html', {"author":author})

@login_required(login_url='login-user')
def update_author(request, author_id):
	author = Author.objects.get(pk=author_id)
	form = AuthorForm(request.POST or None, instance = author )
	if form.is_valid():
		form.save()
		return redirect('view-posts')
	return render(request, 'html_files/update_author.html', {"author":author, "form":form})
	
def delete_author(request, author_id):
	author = Autjor.objects.get(pk=author_id) 
	author.delete()
	return redirect('view-posts')
	
# POST
@login_required(login_url='login-user')
def make_post(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		author = request.user
		post = Post.objects.create(title=title, author=author, write_up=content)
		post.save()
		return redirect('view-posts')
	return render(request, 'html_files/make_post.html', {})

@login_required(login_url='login-user')
def view_posts(request):
	posts = Post.objects.all().order_by('-date')
	return render(request, 'html_files/view_posts.html', {"posts":posts})

@login_required(login_url='login-user')	
def view_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render(request, 'html_files/view_post.html', {"post":post}) 

@login_required(login_url='login-user')	
def update_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	form = PostsForm(request.POST or None, instance = post)
	if form.is_valid():
		form.save()
		return redirect('view-posts')
	return render(request, 'html_files/update_post.html', {"post":post, "form":form})
	
def delete_post(request, post_id):
	post = Posts.objects.get(pk=post_id) 
	post.delete()
	return redirect('view-posts')
	

#if User.objects.filter(email=email).exists():	

@login_required(login_url='login-user')
def add_to_fav(request, pk):
	get_user = request.user
	book_id = Post.objects.get(id=pk)
	x =  book_id in get_user.favorite_book.name_of_book.all()
	print(x)
	get_user.favorite_book.name_of_book.add(book_id)
	return render(request, 'html_files/show_books.html', {'x':x})

@login_required(login_url='login-user')
def show_book(request, pk):
	get_user = User.objects.get(id=pk)
	return render(request, 'html_files/show_books.html', {'get_user':get_user})

@login_required(login_url='login-user')
def rmv_from_fav(request, pk):
	get_user = request.user
	book_id = Post.objects.get(id=pk)
	x =  book_id in get_user.favorite_book.name_of_book.all()
	print(x)
	get_user.favorite_book.name_of_book.remove(book_id)
	return redirect(request.META.get("HTTP_REFERER"))























