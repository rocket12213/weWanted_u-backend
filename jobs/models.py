from django.db          import models
from company.models     import Companise

class Categories(models.Model) :
    category    = models.CharField(max_length=500)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'categories'

class Jobs(models.Model) :
    companise           = models.ForeignKey(Companise, on_delete=models.CASCADE)
    categories          = models.ForeignKey(Categories, on_delete=models.CASCADE)
    position            = models.CharField(max_length=500)
    intro               = models.CharField(max_length=3000)
    main_tasks          = models.CharField(max_length=3000)
    requirements        = models.CharField(max_length=3000)
    preferred_points    = models.CharField(max_length=3000)
    benefits            = models.CharField(max_length=3000)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'jobs'

'''
class Tags(models.Model) :
    skill               = models.CharField(max_length=100)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'tags'
'''
