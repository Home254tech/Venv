from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('psw_checker', views.psw_checker, name='psw_checker'),
    path('psw_maker', views.psw_maker, name='psw_maker'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
     path('login', views.login, name='login'),
     path('logout', views.logout, name='logout'),
    path('test', views.test, name='test'),
    
]
