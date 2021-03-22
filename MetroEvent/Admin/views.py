from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

class DashboardView(View):
    def get(self, request):
        return render(request,'Admin_dashboard.html')