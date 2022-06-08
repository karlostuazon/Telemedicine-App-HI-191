from django.urls import path
from . import views

urlpatterns = [
     path('create-record', views.createRecord, name = 'create-record'),
]