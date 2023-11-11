from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
	
class Post(models.Model):
	title = models.CharField("Title", blank=False, null=False, max_length=300)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	author_name = models.CharField("Author Name", blank=True, null=True, max_length=300)
	date = models.DateTimeField('Date Published', auto_now_add=True)
	write_up = models.TextField("Content", blank=False)
	
	def __str__(self):
		return f'{self.title} by {self.author}'
	

class Favorite_Book(models.Model):
	user=models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	name_of_book=models.ManyToManyField('Post', blank=True)
	

	def __str__(self):
		return f'{self.name_of_book}'


def create_fav_book(sender, instance, created, **kwargs):
	if created:
		fav_book = Favorite_Book(user=instance)
		fav_book.save()

post_save.connect(create_fav_book, sender=User)
