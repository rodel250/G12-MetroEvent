from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from django.contrib import messages

class DashboardView(View):

	def get(self, request):

		return render(request,'METROEVENT_dashboard2.html')

class LandingPageView(View):
	def get(self, request):
		return render(request, 'METROEVENT_landingPage2.html')
