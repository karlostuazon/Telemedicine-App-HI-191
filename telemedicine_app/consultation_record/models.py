import email
from pyexpat import model
from django.db import models
from telemedicine.models import *
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class ConsultationRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)

    consultation_date = models.DateTimeField(null=True, blank=True)

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

    nxt_cons_date = models.DateField(null=True, blank=True)

    link = models.CharField(max_length=100, null=True, blank=True)

    document = models.FileField(upload_to='docus/', null=True, blank=True)

    prescriptions = models.FileField(upload_to='docus/', null=True, blank=True)
    # def __str__(self):
    #     return "{}".format(self.doctor)
    def __str__(self):
        return "{}, {} - {}".format(self.patient.last_name, self.patient.first_name, self.doctor.last_name)


class Documents(models.Model):
    file = models.FileField(upload_to='docus/', null=True, blank=True)
    cons_record = models.ForeignKey(ConsultationRecord, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        self.file + "-" + self.cons_record


# For Video Chat 
class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name