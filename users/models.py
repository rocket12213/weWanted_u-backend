from django.db      import models
from job.models     import Jobs

class Users(models.Model) :
    email       = models.CharField(max_length=20)
    password    = models.CharField(max_length=400)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    job         = models.ManyToManyField(Jobs, through='Follows')

    class Meta :
        db_table = 'users'

class Follows(models.Model) :
    user        = models.ForeignKey(Users, on_delete=models.CASCADE)
    job         = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table ='follows'
