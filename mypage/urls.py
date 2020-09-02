
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypage, name="mypage"),
    path('profile_update/', views.profile_update, name="profile_update"),

]
