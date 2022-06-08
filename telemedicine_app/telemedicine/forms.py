from django import forms
from django.db import models
from django.db.models import fields
from django.forms import *
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import DateField
from django.forms.widgets import *


class UserForm(UserCreationForm):
    attrs = {'class': 'form-control form-control-user', 'id': 'floatingInput',
             'placeholder': 'Enter Password'}
    attrs1 = {'class': 'form-control form-control-user', 'id': 'floatingInput',
             'placeholder': 'Re-Enter Password'}
    password1 = CharField(widget=PasswordInput(attrs=attrs))
    password2 = CharField(widget=PasswordInput(attrs=attrs1))
    email = EmailField(max_length=254, help_text='Required. Input a valid email address.',widget=TextInput(attrs = {'class': 'form-control form-control-user', 'id': 'floatingInput',
             'placeholder': 'Email'}))

    class Meta:
        model = User
        fields =['username', 'password1', 'password2', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Username', 'aria-label': 'Username'}),
        }


class PatientForm(ModelForm):
    birthdate = DateField(
        widget=DateInput(
            attrs={'class': 'form-control datetimepicker-input', 'id': 'dob', 'placeholder': 'Birthdate(mm/dd/yyyy)',
                     'data-target': '#datetimepicker1'},
                     format='%m/%d/%y'
        ),
    )
    class Meta:
        model = Patient
        fields = ['last_name', 'first_name', 'middle_name', 'suffix', 'sex', 'age', 'attending_doctor', 'birthdate']
        widgets={
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'suffix': TextInput(attrs={'class': 'form-control', 'placeholder': 'Suffix'}),
            'sex': Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}),
            'age': TextInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'attending_doctor': Select(attrs={'class': 'form-control', 'placeholder': 'Attending Doctor'}),
        }