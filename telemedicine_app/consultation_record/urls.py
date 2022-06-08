from django.urls import path
from . import views

urlpatterns = [
     path('create-record', views.createRecord, name = 'create-record'),
     path('view-record-patient', views.viewRecordPatient, name = 'view-record-patient'),
     path('view-record-doctor', views.viewRecordDoctor, name = 'view-record-doctor'),
]