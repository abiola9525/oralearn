"""blogproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('java.urls')),
    path('', include('htmlcss.urls')),
    path('', include('pydjango.urls')),
    path('', include('node.urls')),
    path('', include('js.urls')),
    path('', include('gd.urls')),
    path('', include('cpp.urls')),
    
    # user authentications
    path('', user_views.display, name="display"),
    path('course', user_views.course, name="course"),
    path('register?8767y7n6/', user_views.register, name="register"),
    path('profile', user_views.profile, name="profile"),
    path('profile/profile_update', user_views.profile_update, name="profile-update"),
    path('login?8754fcdvtter4di6ft/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
