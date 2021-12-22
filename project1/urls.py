from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login, name='login'),
    path('register', views.register, name='register'),
    path('', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('chinese', views.chinese, name='chinese'),
    path('indian', views.indian, name='indian'),
    path('italian', views.italian, name='italian'),
    path('indian',views.indian,name='indian'),
   
]