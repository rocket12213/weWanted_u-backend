from django.db      import models
from job.models     import Jobs

class Users(models.Model) :
    email       = models.CharField(max_length=20)
    password    = models.CharField(max_length=400)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    job         = models.ManyToManyField(Jobs, through='Follow')

    class Meta :
        db_table = 'users'

class Follow(models.Model) :
    user        = models.ForeignKey(Users, on_delete=models.CASCADE)
    job         = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    follow      = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table ='follow'
