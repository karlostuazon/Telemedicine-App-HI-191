from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from datetime import datetime

from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctor'])
def createRecord(request):
    cons_form = ConsultationForm()
    if(request.method == "POST"):
        cons_form = ConsultationForm(request.POST)
        if(cons_form.is_valid()):
            today = datetime.now()
            temp = cons_form.save(commit=False)
            temp.doctor = request.user.doctor
            temp.consultation_date = today
            temp.save()
            messages.success(request, 'Consultation form submitted!')
            return redirect('create-record')
        else:
            messages.error(request, cons_form.errors)
    data = {
        'cons_form': cons_form
    }
    return render(request, 'consultation_record/create-record.html', data)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Patient'])
def viewRecordPatient(request):
    consultations = ConsultationRecord.objects.filter(patient=request.user.patient)

    data={
        'consultations':consultations,
    }
    return render(request, 'consultation_record/view-record-patient.html', data) 


@login_required(login_url='login')
@allowed_users(allowed_roles=['Patient'])
def viewRecordPatientInfo(request, pk):
    cons = ConsultationRecord.objects.get(id=pk)

    data={
        'cons':cons,
    }
    return render(request, 'consultation_record/view-record-patient-info.html', data) 


@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctor'])
def viewRecordDoctor(request):
    consultations = ConsultationRecord.objects.filter(doctor=request.user.doctor)
    
    data={
        'consultations':consultations,
    }
    return render(request, 'consultation_record/view-record-doctor.html', data) 