from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import AuthorForm, PostsForm
from django.contrib import messages
from .models import Post, Author
from django.conf import settings
from django.core.mail import send_mail

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
	submitted = False
	if request.method == "POST":
		form = PostsForm(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			get_name = form.cleaned_data['author']
			authors = Author.objects.get(first_name=get_name)
			x.author_name = authors.first_name
			x.save()
			messages.success(request, ("Uploaded !!!"))
			return HttpResponseRedirect("/make_post?submitted=True")
	else:
		form = PostsForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'html_files/make_post.html', {"submitted": submitted, "form":form})

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
	
def send_email(request):
	subject = "Django"
	message = "You've been hired"
	from_email = settings.EMAIL_HOST_USER
	receiver = ["abdulmajidadeiza@gmail.com"]
	send_mail(subject, message, from_email, receiver)
	messages.success(request, ("Email sent"))
	return redirect('home')
	