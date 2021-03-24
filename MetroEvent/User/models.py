from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 50, null=False, blank=False,primary_key = True,default = 'default')
    firstname = models.CharField(max_length = 50, null=True, blank=True)
    middlename = models.CharField(max_length = 50, null=True, blank=True)
    lastname = models.CharField(max_length = 50, null=True, blank=True)
    password = models.CharField(max_length = 50, null=True, blank=True)
    emailAddress = models.CharField(max_length = 50, null=True, blank=True)
    gender = models.CharField(max_length = 50, null=True, blank=True)
    birthdate = models.DateField(default = datetime.now(), null=True, blank=True)
    class Meta:
        db_table = "User"
    
class UserRequest(models.Model):
    requestID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,max_length = 50, null = False, blank = False, on_delete = models.CASCADE, related_name = "userID")
    isApprove = models.IntegerField()
    class Meta:
        db_table = "UserRequest"

class Organizer(models.Model):
    organizerID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,max_length = 50, null = False, blank = False, on_delete = models.CASCADE, related_name = "organizerUser")
    class Meta:
        db_table = "Organizer"

class Event(models.Model):
    organizer = models.ForeignKey(Organizer, null = False, blank = False, on_delete = models.CASCADE, related_name = "orgID")
    eventID = models.AutoField(primary_key = True)
    eventName = models.CharField(max_length = 50, null=True, blank=True)
    eventDate = models.CharField(max_length = 50, null=True, blank=True)
    eventParticipants = models.IntegerField()
    class Meta:
        db_table = "Event"

class Participants(models.Model):
    participantsID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,max_length = 50, null = False, blank = False, on_delete = models.CASCADE, related_name = "participantUser")
    event = models.ForeignKey(Event, null = False, blank = False, on_delete = models.CASCADE, related_name = "eventIDs")
    class Meta:
        db_table = "Participants"