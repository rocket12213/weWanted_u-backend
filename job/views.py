import json
from django.http    import JsonResponse
from django.views   import View
from .models        import Categories, Tags, Jobs, JobsToTags
from company.models import Companies, CompaniesImages

class RecruitmentView(View) :
    def get(self, request, job_id) :
        try :
            job = Jobs.objects.select_related('company').prefetch_related('tags').prefetch_related('company__companiesimages_set').get(id=job_id)

            job_info = {
                         "position"          : job.position,
                         "intro"             : job.intro,
                         "main_tasks"        : job.main_tasks,
                         "requirements"      : job.requirements,
                         "preferred_points"  : job.preferred_points,
                         "benefits"          : job.benefits,
                         "dead_line"         : job.dead_line,
                         "job_id"            : job.id
                       }
            company_info = {
                             "company_name"  : job.company.company_name,
                             "main_image"    : job.company.main_image,
                             "logo_image"    : job.company.logo_image,
                             "city"          : job.company.city,
                             "country"       : job.company.country,
                             "full_location" : job.company.full_location,
                             "lat"           : job.company.lat,
                             "lng"           : job.company.lng,
                             "company_id"    : job.company.id
                           }
            company_images = [{
                                "company_image"     : image.company_image, 
                                "company_image_id"  : image.company_id
                              } for image in job.company.companiesimages_set.all()]
            tags = [{
                      "skill"     : tag.skill, 
                      "tag_id"    : tag.id
                    } for tag in job.tags.all()]
            data = {
                     "job"               : job_info,
                     "company"           : company_info,
                     "company_images"    : company_images,
                     "tags"              : tags
                   }
            return JsonResponse(data, status=200)
        except :
            return JsonResponse({"message":"NOT Found"}, status=404)

class JobListView(View) : 
    def get(self, request, category_id) :
        if (category_id == 1 or category_id == 2) :
            job_list = Jobs.objects.filter(category_id=category_id).select_related('company').prefetch_related('tags')

            data=[]
            for job in job_list :
                job_info = {
                            "position"      : job.position,
                            "job_id"        : job.id,
                            "dead_line"     : job.dead_line
                          }
                company = {
                            "company_name"  : job.company.company_name,
                            "main_image"    : job.company.main_image,
                            "city"          : job.company.city,
                            "country"       : job.company.country,
                            "company_id"    : job.company.id
                          }
                tags = [{
                          "skill" : tag.skill, 
                          "tag_id" : tag.id
                        } for tag in job.tags.all()]
                job_data = {
                             "job" : job_info, 
                             "company" : company, 
                             "tags" : tags
                           }
                data.append(job_data)
            return JsonResponse({"data" : data}, status=200)

        elif(category_id == 3) :
            category_list = Categories.objects.all()
            main_data=[]

            for category in category_list :
                job_list = Jobs.objects.filter(category_id=category.id).select_related('company').prefetch_related('tags')
                for job in job_list :
                    job_info = {
                                "position"      : job.position,
                                "job_id"        : job.id,
                                "dead_line"     : job.dead_line
                               }
                    company = {
                                "company_name"  : job.company.company_name,
                                "main_image"    : job.company.main_image,
                                "city"          : job.company.city,
                                "country"       : job.company.country,
                                "company_id"    : job.company.id
                              }
                    tags = [{
                             "skill" : tag.skill, 
                             "tag_id" : tag.id
                            } for tag in job.tags.all()]
                    job_data = {
                                "job" : job_info, 
                                "company" : company, 
                                "tags" : tags
                               }
                    main_data.append(job_data)
            return JsonResponse({"data" : main_data}, status=200)
