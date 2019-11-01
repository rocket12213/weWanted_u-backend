from django.db import models

class Users(models.Model) :
    email      = models.CharField(max_length=20)
    password   = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'users'
             
# Create your models here.
