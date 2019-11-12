from django.db      import models
from users.models   import Users
from job.models     import Categories
from company.models import Companies

class Careers(models.Model) :
    career      = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'careers'

class Moods(models.Model) :
    mood        = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'moods'

class Routes(models.Model) :
    route       = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'routes'

class TestLevels(models.Model) :
    level       = models.IntegerField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table ='testlevels'

class Results(models.Model) :
    result      = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'results'

class Reviews(models.Model) :
    question    = models.TextField()
    answer      = models.TextField()
    review      = models.TextField()
    user        = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    company     = models.ForeignKey(Companies, on_delete=models.CASCADE)
    category    = models.ForeignKey(Categories, on_delete=models.CASCADE)
    career      = models.ForeignKey(Careers, on_delete=models.CASCADE)
    mood        = models.ForeignKey(Moods, on_delete=models.CASCADE)
    route       = models.ForeignKey(Routes, on_delete=models.CASCADE)
    test_level  = models.ForeignKey(TestLevels, on_delete=models.CASCADE)
    result      = models.ForeignKey(Results, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'reviews'



