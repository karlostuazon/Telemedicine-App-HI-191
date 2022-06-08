from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class ConsultationForm(forms.ModelForm):
    mobile = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False,
    )
    mobile.widget.attrs = {'class': 'form-control', 'id': 'mobile_num', 'placeholder': 'Mobile (+63)'}
    class Meta:
        model = ConsultationRecord
        fields = '__all__'
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Patient'}),
            'doctor': forms.HiddenInput(attrs={'type': 'hidden'}),

            'consultation_date': forms.HiddenInput(attrs={'type': 'hidden'}),

            'p_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'landline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Landline'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),

            'curr_med': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make'}),
            'temp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make'}),
            'allergies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make'}),
            'pres_prob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make'}),
            'assessments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make'}),
            'plan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make'}),

            'nxt_cons_date': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Date', 'type': 'date'}),
        }