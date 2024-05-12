"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # new I tried to add this line include so I can see homepage
from users import views as user_views #I added this line to register a user
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), # new here is what I added Mr.Deepak
    path('register/', user_views.register, name="user-register"), #I added this line to register a user
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="user-login"), 
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    path('profile/', user_views.profile, name="user-profile"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #This is for the images to show up on the homepage
