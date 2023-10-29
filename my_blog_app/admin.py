from django.contrib import admin
from .models import Author, Post

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name")
	fields = (("first_name", "last_name"), "email")

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
	list_display = ("title", "author")
	fields = (("title", "author"), "write_up", "date")