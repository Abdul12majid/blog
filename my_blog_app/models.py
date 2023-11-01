from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
	
class Post(models.Model):
	title = models.CharField("Title", blank=False, null=False, max_length=300)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	date = models.DateTimeField('Date Published', auto_now_add=True)
	write_up = models.TextField("Content", blank=False)
	
	def __str__(self):
		return f'{self.title} by {self.author}'
	

class Favorite_Book(models.Model):
	user=models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	name_of_book=models.ManyToManyField('Post', blank=True)
	

	def __str__(self):
		return f'{self.name_of_book}'