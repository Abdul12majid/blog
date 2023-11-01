from django.contrib import admin
from .models import Post, Favorite_Book
from django.contrib.auth.models import Group, User

# Register your models here.

admin.site.unregister(Group)


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
	list_display = ("title", "author")
	fields = (("title", "author"), "write_up",)

class ProfileInline(admin.StackedInline):
	model=Favorite_Book

class UserAdmin(admin.ModelAdmin):
	model=User
	fields=('username',)
	inlines=[ProfileInline]

#admin.site.register(Favorite_Book)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)