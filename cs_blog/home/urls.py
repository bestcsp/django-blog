from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('Search', views.Search,name='Search'),
    path('signup', views.HandleSignup,name='HandleSignup'),
    path('login', views.HandleLogin,name='HandleLogin'),
    path('logout', views.HandleLogout,name='HandleLogout'),
    path('profile', views.profile,name='profile'),

    
]