"""
URL configuration for myproject project.

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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('book/', views.book, name='book'),
    path('booking_success/', views.booking, name='booking_success'),
    path('view/', views.view_bookings, name='view_bookings'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('book_done/', views.book_done, name='book_done'),
    path('login_done/', views.login_done, name='login_done'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),




]



