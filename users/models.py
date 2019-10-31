from django.db import models

class Users(models.Model) :
	email    = models.CharField(max_length=20)
	password = models.Charfield(max_length=400)

	class Meta :
		db_table = 'users'

# Create your models here.
