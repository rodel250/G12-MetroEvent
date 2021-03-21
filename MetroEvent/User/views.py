from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages




class DashboardView(View):

	def get(self, request):

		return render(request,'METROEVENT_dashboard2.html')

	

class LandingPageView(View):
	def get(self, request):
		return render(request, 'METROEVENT_landingPage2.html')

	def post(self, request):
		form = UserForm(request.POST)
		if request.method == 'POST':
			uname = request.POST.get("UserName")
			fname = request.POST.get("FirstName")
			lname = request.POST.get("LastName")
			mname = request.POST.get("MiddleName")
			pword = request.POST.get("Password")
			gender1 = "test"
			emailAdd = request.POST.get("Email")
			bdate = request.POST.get("Birthdate")
			form = User(username = uname, firstname = fname, middlename = mname, lastname = lname, password = pword, emailAddress = emailAdd, gender = gender1, birthdate = bdate)
			form.save()
		return render(request, 'METROEVENT_landingPage2.html')
