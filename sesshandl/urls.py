from django.urls import include, path
from django.contrib.auth import urls
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('accouns/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup', views.signup, name='signup'),
    #path('/signup', 'registratiion/signup.html', name='signup')
]
