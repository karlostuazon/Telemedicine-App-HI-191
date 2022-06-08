from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
# Create your views here.

@unauthenticated_user
def createRecord(request):
    return render(request, 'consultation_record/create-record.html')