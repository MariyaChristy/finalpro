"""
URL configuration for Final_MovieProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from Final_MovieProject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MovieApp.urls')),
    path('search/',include('search_app.urls')),
    path('credentials/',include('credentials.urls')),
    path('profileapp/',include('profileapp.urls')),
]+static(settings.STATIC_ROOT,document_root=settings.STATIC_ROOT)\
              +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

