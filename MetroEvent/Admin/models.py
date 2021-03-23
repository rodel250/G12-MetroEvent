from django.db import models
from User.models import User

# Create your models here.
class Admin(models.Model):
    admin = models.IntegerField(null=False, blank=False,primary_key = True,default = 'default')
    user = models.ForeignKey(User,max_length = 50, null = False, blank = False, on_delete = models.CASCADE, related_name = "User")
    class Meta:
        db_table = "Admin"