from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import *
from User.models import UserRequest,Organizer
from django.contrib import messages

# Create your views here.

class DashboardView(View):
    def get(self, request):
        userRequest = UserRequest.objects.filter(isApprove = 2)
        
        context = {
            'requests' : userRequest    
        }
        return render(request,'Admin_dashboard.html',context)
    
    def post(self, request):
        if request.method == 'POST':
            if 'btnApprove' in request.POST:
                username = request.POST.get("hiddenID")
                organizerIns = Organizer.objects.create(user_id = username)
                updateRequest = UserRequest.objects.filter(user_id = username).update(isApprove = 1)
            elif 'btnDisapprove' in request.POST:
                username = request.POST.get("hiddenID")
                deleteRequest = UserRequest.objects.filter(user_id = username).delete()
        return redirect('Admin:dashboard_view')
        