import json
from django.http    import JsonResponse
from django.views   import View
from .models        import Categories, Tags, Jobs, JobsToTags
from company.models import Companies, CompaniesImages

class JobDetailPageView(View) :
    def get(self, request, jobs_id) :
        try :
            job_query_set               = Jobs.objects.get(pk=jobs_id)
            company_query_set           = Companies.objects.get(id=job_query_set.companies_id)
            company_images_query_set    = company_query_set.companiesimages_set.all()
            tags_query_set              = JobsToTags.objects.filter(jobs_id=jobs_id)


            job = {
                    "position"          : job_query_set.position,
                    "intro"             : job_query_set.intro,
                    "main_tasks"        : job_query_set.main_tasks,
                    "requirements"      : job_query_set.requirements,
                    "preferred_points"  : job_query_set.preferred_points,
                    "benefits"          : job_query_set.benefits,
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

            company_images  = []
            for image in company_images_query_set :
                company_images.append({
                    "company_image"     : image.company_image,
                    "company_image_id"  : image.id
                })

            tags =[]
            for tag in tags_query_set :
                tags.append({
                    "skill"     : Tags.objects.get(id = tag.tags_id).skill,
                    "tag_id"    : tag.tags_id
                })

            job_info                    = {}
            job_info["job"]             = job
            job_info["company"]         = company
            job_info["company_images"]  = company_images
            job_info["tags"]            = tags
            return JsonResponse(job_info, status=200)

        except :
            return JsonResponse({"message":"NOT Found!"}, status=404)
