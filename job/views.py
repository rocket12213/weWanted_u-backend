import json
from django.http    import JsonResponse
from django.views   import View
from .models        import Categories, Tags, Jobs, JobsToTags
from company.models import Companies, CompaniesImages

class JobDetailPageView(View) :
    def get(self, request, job_id) :
        try :
            job_query_set               = Jobs.objects.get(pk=job_id)
            company_query_set           = Companies.objects.get(id=job_query_set.company_id)
            company_images_query_set    = company_query_set.companiesimages_set.all()
            tags_query_set              = JobsToTags.objects.filter(job_id=job_id)

            job = {
                    "position"          : job_query_set.position,
                    "intro"             : job_query_set.intro,
                    "main_tasks"        : job_query_set.main_tasks,
                    "requirements"      : job_query_set.requirements,
                    "preferred_points"  : job_query_set.preferred_points,
                    "benefits"          : job_query_set.benefits,
                    "dead_line"         : job_query_set.dead_line,
                    "job_id"            : job_query_set.id

                  }

            company = {
                        "company_name"  : company_query_set.company_name,
                        "main_image"    : company_query_set.main_image,
                        "logo_image"    : company_query_set.logo_image,
                        "city"          : company_query_set.city,
                        "country"       : company_query_set.country,
                        "full_location" : company_query_set.full_location,
                        "lat"           : company_query_set.lat,
                        "lng"           : company_query_set.lng,
                        "company_id"    : company_query_set.id
                      }

            company_images = [{"company_image" : image.company_image, "company_image_id" : image.id} for image in company_images_query_set]
            tags =[{"skill" : Tags.objects.get(id = tag.tag_id).skill, "tag_id" : tag.tag_id} for tag in tags_query_set]

            job_info                    = {}
            job_info["job"]             = job
            job_info["company"]         = company
            job_info["company_images"]  = company_images
            job_info["tags"]            = tags
            return JsonResponse(job_info, status=200)

        except :
            return JsonResponse({"message":"NOT Found!"}, status=404)

class JobsMainPageView(View) : 
    def get(self, request, category_id) :
        if (category_id == 1 or category_id == 2) :
            category_query_set = Categories.objects.get(pk=category_id)
            job_list_query_set = category_query_set.jobs_set.all()
            
            main_data=[]
            for job in job_list_query_set :
                company_query_set = Companies.objects.get(pk=job.company_id)
                tags_query_set = JobsToTags.objects.filter(job_id=job.id)
              
                job_info = {
                            "position"      : job.position,
                            "job_id"        : job.id
                           }
                
                company = {
                            "company_name"  : company_query_set.company_name,
                            "main_image"    : company_query_set.main_image,
                            "city"          : company_query_set.city,
                            "country"       : company_query_set.country,
                            "company_id"    : company_query_set.id
                          }

                tags =[{"skill" : Tags.objects.get(id = tag.tag_id).skill, "tag_id" : tag.tag_id} for tag in tags_query_set]
                job_data ={"job" : job_info, "company" : company, "tags" : tags}
                main_data.append(job_data)
            return JsonResponse({"data" : main_data}, status=200)

        elif(category_id == 3) :
            category_query_set = Categories.objects.all()
            main_data=[]
            for category in category_query_set :
                job_list_query_set = category.jobs_set.all()
                for job in job_list_query_set :
                    company_query_set = Companies.objects.get(pk=job.company_id)
                    tags_query_set = JobsToTags.objects.filter(job_id=job.id)

                    job_info = {
                                "position"      : job.position,
                                "job_id"        : job.id
                               }

                    company = {
                                "company_name"  : company_query_set.company_name,
                                "main_image"    : company_query_set.main_image,
                                "city"          : company_query_set.city,
                                "country"       : company_query_set.country,
                                "company_id"    : company_query_set.id
                              }
                    tags = [{"skill" : Tags.objects.get(id= tag.tag_id).skill, "tag_id" : tag.tag_id} for tag in tags_query_set]
                    job_data = {"job" : job_info, "company" : company, "tags" : tags}
                    main_data.append(job_data)
            return JsonResponse({"data" : main_data}, status=200)

