from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_blog_app.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('api/', include('api.urls')),

    path('accounts/', include('allauth.urls')),
    path('', include('my_blog_app.urls')),

]
