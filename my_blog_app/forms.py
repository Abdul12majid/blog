from django import forms
from django.forms import ModelForm
from .models import Post

class PostsForm(ModelForm):
	class Meta:
		fields = ('title', 'author', 'write_up')
		model = Post


