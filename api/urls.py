from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('get_post/<int:pk>', views.post, name="post"),
    path('make_post/', views.make_post, name="make-post"),
    path('create_account/', views.create_account, name="create-account"),
    path('login_account/', views.login_account, name="login-account"),

    path('user_details/<int:pk>', views.user_details, name="user-details"),
    path('post_details/<int:pk>', views.post_details, name="post-details"),

    path('delete_post/<int:pk>', views.delete_post, name="delete-post"),
    path('delete_user/<int:pk>', views.delete_user, name="delete-user"),

]