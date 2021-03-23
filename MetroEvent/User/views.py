from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

uniuser=None


class DashboardView(View):

	def get(self, request):
		username = uniuser()
		#userinfo = User.objects.filter(username=username)
		test = User.objects.raw('SELECT * FROM user,userrequest WHERE user.username = "'+ username +'" and user.username = userrequest.user_id')

		context = {
				'userinfo' : test
			}

		return render(request,'METROEVENT_dashboard2.html',context)

	def post(self, request):
		if request.method == 'POST':
			if 'btnUpdate' in request.POST:
				print('update profile button clicked')

				uname = request.POST.get("username")
				fname = request.POST.get("first_name")
				mname = request.POST.get("middle_name")
				lname = request.POST.get("last_name")
				eml = request.POST.get("email")
				gdr = request.POST.get("gender")
				birth = request.POST.get("bday")
				pword = request.POST.get("password")

				update_user = User.objects.filter(username = uname).update(firstname = fname, middlename = mname, lastname = lname, emailAddress = eml, gender = gdr, birthdate = birth, password = pword)
				messages.success(request, 'User Info has been Updated')
				
				global uniuser
				def uniuser():
					return uname
				return redirect('User:dashboard_view')

			elif 'btnDelete' in request.POST:
				uid = request.POST.get("userid")
				users = User.objects.filter(username=uniuser()).delete()
				messages.success(request, 'Account has been Deleted')
				return redirect('User:landing_view')
			
			elif 'btnOrganizer' in request.POST:
				try:
					Userdetails = UserRequest.objects.get(user_id=uniuser())
					messages.success(request, 'You already sent a request!')
					return redirect('User:dashboard_view')
				
				except UserRequest.DoesNotExist:
					requestInstance = UserRequest.objects.create(user_id = uniuser(), isApprove = 0)
					messages.success(request, 'Succesfully Requested')
					return redirect('User:dashboard_view')
					

				
		

			'''elif 'btnActivate' in request.POST:
				uid = request.POST.get("userid")
				users = User.objects.filter(id=uid).update(Status = "Active")
				messages.success(request, 'User has been Active')
				return redirect('UI:dashboard_view')'''

			

	

class LandingPageView(View):
	def get(self, request):
		return render(request, 'METROEVENT_landingPage2.html')

	def post(self, request):
		form = UserForm(request.POST)
		if form.is_valid():
			if 'btnRegister' in request.POST:
				uname = request.POST.get("UserName")
				fname = request.POST.get("FirstName")
				lname = request.POST.get("LastName")
				mname = request.POST.get("MiddleName")
				pword = request.POST.get("Password")
				gender1 = request.POST.get("Gender")
				emailAdd = request.POST.get("Email")
				bdate = request.POST.get("Birthdate")
				try:
					Userdetails = User.objects.get(username=uname)
					messages.success(request, 'Username already Exist, Try another Username')
					return redirect('User:landing_view')

				except User.DoesNotExist:
					form = User(username = uname, firstname = fname, middlename = mname, lastname = lname, password = pword, emailAddress = emailAdd, gender = gender1, birthdate = bdate)
					form.save()
					messages.success(request, 'User '+ uname +' was registered successfully!')
					return redirect('User:landing_view')

			elif 'Loginclick' in request.POST:
				if request.POST['usern'] == "Admin" and request.POST['passw'] == "Admin":
						return redirect('Admin:dashboard_view')
				else:		
					try:				
						
						Userdetails = User.objects.get(username=request.POST['usern'],password=request.POST['passw'])
						request.session['usern']=Userdetails.username
						request.session['passw']=Userdetails.password
						user = Userdetails.username
						global uniuser
						def uniuser():
							return user

						return redirect('User:dashboard_view')
						
					except User.DoesNotExist:
						messages.success(request, 'Invalid Account, Please Enter a Valid account')
						return redirect('User:landing_view')
		
		else:
			return HttpResponse('not valid')


