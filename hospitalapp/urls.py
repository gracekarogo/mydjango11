from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner-page/', views.inner, name='inner'),
    path('register/', views.register, name='Register'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('details/', views.details, name='details'),
    path('users/', views.users, name='users'),


    ]
