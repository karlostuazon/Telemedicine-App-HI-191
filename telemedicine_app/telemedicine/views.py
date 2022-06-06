from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    if user.groups.filter(name='Patient User').exists():
                        login(request, user)
                        return redirect('homePatient')
                    else:
                        login(request, user)
                        return redirect('home')
                else:
                    messages.info(request, 'Username or password is incorrect. Please try again.')
        context = {}
        return render(request, 'telemedicine/login.html', context)


@login_required(login_url='login')
def homePage(request):
    patients = Patient.objects.all()
    #patientFilter = PatientFilter(request.GET, queryset=patients)
    #patients = patientFilter.qs

    #physicians = Physician.objects.all()
    data = {
        'patients': patients,
    }

    return render(request, "telemedicine/home.html", data)


def logoutUser(request):
	logout(request)
	return redirect('login')
