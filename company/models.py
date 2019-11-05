from django.db import models

class Companise(models.Model) :
    company_name    = models.CharField(max_length = 300)
    main_image      = models.URLField(max_length = 3000, null = True)
    logo_image      = models.URLField(max_length = 3000, null = True)
    city            = models.CharField(max_length = 100)
    country         = models.CharField(max_length = 100)
    full_location   = models.CharField(max_length = 1000)
    lat             = models.DecimalField(max_digits = 35, decimal_places=30, null = True)
    lng             = models.DecimalField(max_digits = 35, decimal_places=30, null = True)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)

    class Meta :
        db_table = "companise"

class CompaniseImages(models.Model) :
    company         = models.ForeignKey(Companise, on_delete=models.CASCADE)
    company_img     = models.URLField(max_length = 3000)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now =True)

    class Meta :
        db_table = "companise_images"
