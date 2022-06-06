from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    cell_no = PhoneNumberField(null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    hospital_affliations = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.last_name + " - "  + self.specialization


class Patient(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    suffix = models.CharField(max_length=2, null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, choices=SEX)
    birthdate = models.DateField(null=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    attending_doctor = models.ForeignKey(Doctor, related_name="docpatient", on_delete=models.CASCADE, null=True, blank=True)
    documents = models.FileField(upload_to='docus/', null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
