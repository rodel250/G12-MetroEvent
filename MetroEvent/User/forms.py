from django import forms
from .models import *

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ()


class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = ()

class NotificationForm(forms.ModelForm):

	class Meta:
		model = Notification
		fields = ()
