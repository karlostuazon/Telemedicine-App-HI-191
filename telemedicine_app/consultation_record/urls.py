from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
     path('create-record', views.createRecord, name = 'create-record'),
     path('view-record-patient', views.viewRecordPatient, name = 'view-record-patient'),
     path('view-record-doctor', views.viewRecordDoctor, name = 'view-record-doctor'),
     path('view-record-doctor-info/<str:pk>', views.viewRecordDoctorInfo, name = 'view-record-doctor-info'),
     path('view-record-patient-info/<str:pk>', views.viewRecordPatientInfo, name = 'view-record-patient-info'),
     path('consult/<str:pk>', views.consult, name = 'consult'),
     path('document-upload/<str:pk>', views.uploadDocus, name = 'document-upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
