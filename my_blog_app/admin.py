from django.contrib import admin
from .models import Author, Post, Favorite_Book
from django.contrib.auth.models import Group, User

# Register your models here.

admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
	model=Favorite_Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name")
	fields = (("first_name", "last_name"), "email")

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
	list_display = ("title", "author")
	fields = (("title", "author"), "write_up", "date",)

class UserAdmin(admin.ModelAdmin):
	model=User
	fields=('username',)
	inlines=[ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)