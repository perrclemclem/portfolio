from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home-page"),
    path('about/', aboutUs, name="about-page"),
    path('contact/', contact, name="contact-page"),
    path('showcontact/', showContact, name='showcontact-page'),
    path('register/', userRegist, name="register-page"),
    path('profile/', userProfile, name="profile-page"),
    path('editprofile/', editProfile, name="editprofile-page"),
    path('action/<int:cid>/', actionPage, name="action-page"),
    path('addproduct/', addProduct, name="addproduct-page")
]