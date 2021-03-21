from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 50, null=False, blank=False,primary_key = True,default = 'default')
    firstname = models.CharField(max_length = 50, null=True, blank=True)
    middlename = models.CharField(max_length = 50, null=True, blank=True)
    lastname = models.CharField(max_length = 50, null=True, blank=True)
    password = models.CharField(max_length = 50, null=True, blank=True)
    emailAddress = models.CharField(max_length = 50, null=True, blank=True)
    gender = models.CharField(max_length = 50, null=True, blank=True)
    birthdate = models.DateField()
    class Meta:
        db_table = "User"