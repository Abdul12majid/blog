from django import forms
from django.forms import ModelForm
from .models import Post, Author

class AuthorForm(ModelForm):
	class Meta:
		fields = ('first_name', 'last_name', 'email')
		model = Author

class PostsForm(ModelForm):
	class Meta:
		fields = ('title', 'author', 'write_up')
		model = Post


