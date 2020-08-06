from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import (
	PersonCreateView,
	PersonsListView,
)
from . import views as views

urlpatterns = [
	path('main/', PersonsListView.as_view(), name='index'),
	path('', views.register, name='login'),
	# path('login/', auth_views.LoginView.as_view(template_name='post/login.html'), name='login'),
	# path('logout/', auth_views.LogoutView.as_view(template_name='post/logout.html'), name='logout'),
	path('new/', PersonCreateView.as_view(), name='create'),
]