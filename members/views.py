from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Login Successful'))
			return redirect('home')
		else:
			messages.success(request, ('Error Logging In'))
			return redirect('login-user')
	else:
		return render(request, 'auth_files/login.html', {})

def register_user(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data['username']
			password= form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration successful"))
			return redirect('home')
		else:
			form = UserCreationForm()
			messages.success(request, ("Problem with your details"))
			return redirect('register-user')
	return render(request, 'auth_files/register_user.html', {"form":form})
	