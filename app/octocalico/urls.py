from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register', views.register, name='register' ),
    path('custom',views.custom , name= 'custom'),
    path('success',views.success , name= 'success'),
    path('home',views.home , name= 'home'),
    path('',views.home , name= 'home'),
]
