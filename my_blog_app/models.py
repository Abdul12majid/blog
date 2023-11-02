from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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


'''
		class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	follows=models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
	date_modified=models.DateTimeField(User, auto_now=True)
	profile_image=models.ImageField(null=True, blank=True, upload_to='images/')
	profile_bio=models.CharField(null=True, blank=True, max_length=500)
	profile_link=models.CharField(null=True, blank=True, max_length=100)

	def __str__(self):
		return self.user.username

def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile=Profile(user=instance)
		user_profile.save()
		user_profile.follows.set([instance.profile.id])
		user_profile.save()
post_save.connect(create_profile, sender=User)
'''

def create_fav_book(sender, instance, created, **kwargs):
	if created:
		fav_book = Favorite_Book(user=instance)
		fav_book.save()

post_save.connect(create_fav_book, sender=User)
