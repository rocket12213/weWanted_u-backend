from django.db          import models
from company.models     import Companies

class Categories(models.Model) :
    category    = models.CharField(max_length=500)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'categories'

class Tags(models.Model) :
    skill               = models.CharField(max_length=100)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'tags'

class Jobs(models.Model) :
    company             = models.ForeignKey(Companies, on_delete=models.CASCADE)
    category            = models.ForeignKey(Categories, on_delete=models.CASCADE)
    position            = models.CharField(max_length=1000, null=True)
    intro               = models.TextField(null=True)
    main_tasks          = models.TextField(null=True)
    requirements        = models.TextField(null=True)
    preferred_points    = models.TextField(null=True)
    benefits            = models.TextField(null=True)
    dead_line           = models.CharField(max_length=1000, null=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    tags                = models.ManyToManyField(Tags, through='JobsToTags')

    class Meta :
        db_table = 'jobs'

class JobsToTags(models.Model) :
    job                 = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    tag                 = models.ForeignKey(Tags, on_delete=models.CASCADE)
    created_at          = models.DateTimeField(auto_now_add=True)

    class Meta :
        db_table = 'jobs_to_tags'
