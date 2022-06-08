from pyexpat import model
from django.db import models
from telemedicine.models import *

# Create your models here.

class ConsultationRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.patient + " - "  + self.doctor