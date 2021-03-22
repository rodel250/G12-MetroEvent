from django.db import models
from User.models import User

# Create your models here.
class Admin(models.Model):
    uesrID = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE, related_name = "User")
    class Meta:
        db_table = "Admin"