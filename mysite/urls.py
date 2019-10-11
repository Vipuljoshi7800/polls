
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from polls import views
from django.urls import path 


urlpatterns = [
    path('', views.post_create, name='post_new'),
    path('post', views.post_index, name='post'),
    path('post/create', views.post_create, name='post.create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),


    # path('fetch',views.post_fetch, name='post_fetch')
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
]