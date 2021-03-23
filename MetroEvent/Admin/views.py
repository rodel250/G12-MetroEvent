from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import *
from User.models import UserRequest
from django.contrib import messages

# Create your views here.

class DashboardView(View):
    def get(self, request):
        userRequest = UserRequest.objects.filter(isApprove = 0)
        context = {
            'requests' : userRequest
        }
        return render(request,'Admin_dashboard.html',context)
    
    def post(self, request):
        if request.method == 'POST':
            if 'btnYes' in request.POST:
                username = request.POST.get("hiddenID")
                print(username)
        return redirect('Admin:dashboard_view')