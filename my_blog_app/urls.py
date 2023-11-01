from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register_author', views.register_author, name="register-author"),
    path('make_post', views.make_post, name='make-post'),
    path('view_posts', views.view_posts, name='view-posts'),
    path('view_post/<post_id>', views.view_post, name='view-post'),
    path('update_post/<post_id>', views.update_post, name='update-post'),
    path('delete_post/<post_id>', views.delete_post, name='delete-post'),
    path('view_author/<author_id>', views.view_author, name='view-author'),
    path('update_author/<author_id>', views.update_author, name='update-author'),
    path('delete_author/<author_id>', views.delete_author, name='delete-author'),
    
    path('add_to_fav/<int:pk>', views.add_to_fav, name='add-to-fav'),
    path('show_book/<int:pk>', views.show_book, name='show-books'),
    path('rmv_from_fav/<int:pk>', views.rmv_from_fav, name='rmv-from-fav'),
]
