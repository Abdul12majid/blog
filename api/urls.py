from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('get_post/<int:pk>', views.post, name="post"),

]