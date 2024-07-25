from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('blog',views.blog,name="blog"),
    path('blog_detail',views.blog_details,name="blog_details"),
    path('service_details',views.service_details,name="service_details"),
    path('starter_page',views.starter_page,name="starter_page"),
]