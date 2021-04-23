from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # Page url
    path('', views.IndexPage, name="indexpage"),
    # function url
    path('register/',views.RegisterUser,name="register"),
]
