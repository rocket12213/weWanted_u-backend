from django.db        import models
from users.models     import Users


class SavingTypes(models.Model) :
    saving_type = models.CharField(max_length=15)

class Resume(models.Model) :
    saving_type  = models.ForeignKey(SavingTypes, on_delete=models.CASCADE)
    title        = models.CharField(max_length=30) 
    phone        = models.CharField(max_length=10)
    email        = models.CharField(max_length=20)
    blog         = models.URLField(max_length=50)
    about_me     = models.TextField()	
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True) 

class Portfolio(models.Model) :
    user	= models.ForeignKey(Users, on_delete=models.CASCADE)
    resume	= models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class Projects(models.Model) : #리스트 요소(한 resume 안에 여러개의 프로 젝트)
    resume        = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=30)
    github        = models.URLField(max_length=3000)
    description   = models.TextField()
    what_did_i_do = models.TextField()
    tech_stack    = models.TextField()

