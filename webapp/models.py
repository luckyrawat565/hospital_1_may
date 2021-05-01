
from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length = 50 , primary_key = True)
    password  = models.CharField(max_length = 20)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    create_time = models.TimeField(auto_now = False, auto_now_add = True)
    modify_time = models.TimeField(auto_now = True, auto_now_add = False)

