from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
	first_name = models.CharField("Name", blank=False, max_length=50)
	last_name = models.CharField("Last Name", blank=False, max_length=50)
	email = models.EmailField("Email Address", blank=False)
	
	def __str__(self):
		return f'{self.first_name}'
	
class Post(models.Model):
	title = models.CharField("Title", blank=False, null=False, max_length=300)
	author = models.ForeignKey(Author, blank=False, on_delete = models.CASCADE)
	author_name = models.CharField('Writer', max_length=50, null=True, blank=True)
	date = models.DateTimeField('Date Published', default=datetime.now())
	write_up = models.TextField("Content", blank=False)
	
	def __str__(self):
		return f'{self.title} by {self.author}'
	

class Favorite_Book(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	name_of_book=models.ManyToManyField('Post', blank=True)
	xxx = models.CharField("Title", blank=True, null=True, max_length=300)

	def __str__(self):
		return f'{self.name_of_book}'