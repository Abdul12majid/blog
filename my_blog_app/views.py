from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PostsForm
from django.contrib import messages
from .models import Post, Favorite_Book
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request, "html_files/index.html", {})
	
def register_author(request):
	submitted = False
	if request.method == "POST":
		form = AuthorForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ("Registered !!!"))
			return HttpResponseRedirect("/register_author?submitted=True")
	else:
		form = AuthorForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'html_files/register_author.html', {"submitted":submitted, "form":form})

def view_author(request, author_id):
	author = Author.objects.get(pk=author_id)
	return render(request, 'html_files/view_author.html', {"author":author})

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

def make_post(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		author = request.user
		post = Post.objects.create(title=title, author=author, write_up=content)
		post.save()
		return redirect('view-posts')
	return render(request, 'html_files/make_post.html', {})

def view_posts(request):
	posts = Post.objects.all()
	return render(request, 'html_files/view_posts.html', {"posts":posts})
	
def view_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render(request, 'html_files/view_post.html', {"post":post}) 
	
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

def add_to_fav(request, pk):
	get_user = request.user
	book_id = Post.objects.get(id=pk)
	x =  book_id in get_user.favorite_book.name_of_book.all()
	print(x)
	get_user.favorite_book.name_of_book.add(book_id)
	return render(request, 'html_files/show_books.html', {'x':x})

def show_book(request, pk):
	get_user = User.objects.get(id=pk)
	return render(request, 'html_files/show_books.html', {'get_user':get_user})

def rmv_from_fav(request, pk):
	get_user = request.user
	book_id = Post.objects.get(id=pk)
	x =  book_id in get_user.favorite_book.name_of_book.all()
	print(x)
	get_user.favorite_book.name_of_book.remove(book_id)
	return redirect(request.META.get("HTTP_REFERER"))























