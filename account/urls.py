from account.views import login_user, register_user
from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user ,name='register'),
]