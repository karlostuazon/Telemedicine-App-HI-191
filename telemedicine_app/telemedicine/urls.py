from django.urls import path
from . import views

urlpatterns = [
     path('', views.loginPage, name = 'login'),
     path('home/', views.homePage, name = 'home'),
     path('logout/', views.logoutUser, name = 'logout'),
     path('register-patient/', views.registerPatient, name = 'register-patient'),
     path('register-doctor/', views.registerDoctor, name = 'register-doctor'),
]