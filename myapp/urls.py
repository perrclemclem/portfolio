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
    path('addproject/', addProject, name="addproject-page"),
    path('competences/', competences, name="competences-page"),
    path('competence1/', competence1, name="competence1-page"),
    path('competence2/', competence2, name="competence2-page"),
    path('competence3/', competence3, name="competence3-page"),
    path('competence4/', competence4, name="competence4-page"),
    path('cv/', cv, name="cv-page"),
    path('projet/<int:cid>/', projectPage, name="project-page"),
]