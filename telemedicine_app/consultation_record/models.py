import email
from pyexpat import model
from django.db import models
from telemedicine.models import *
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class ConsultationRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)

    consultation_date = models.DateTimeField(null=True)

    p_address = models.CharField(max_length=100, null=True, blank=True)
    landline = models.CharField(max_length=100, null=True, blank=True)
    mobile = PhoneNumberField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=256, null=True, blank=True)

    curr_med = models.CharField(max_length=100, null=True, blank=True)
    temp = models.CharField(max_length=100, null=True, blank=True)
    allergies = models.CharField(max_length=100, null=True, blank=True)
    pres_prob = models.CharField(max_length=100, null=True, blank=True)
    assessments = models.CharField(max_length=100, null=True, blank=True)
    plan = models.CharField(max_length=100, null=True, blank=True)

    nxt_cons_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.patient + " - "  + self.doctor