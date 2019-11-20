import json

from django.http    import JsonResponse
from django.views   import View

from .models        import Categories, Tags, Jobs, JobsToTags
from company.models import Companies, CompaniesImages
from users.models   import Users, Follows
from users.utils    import auth_required_decorator

class JobView(View) :
    @auth_required
    def get(self, request, job_id) :
        user_id = request.user.id
        
        try:
            job = Jobs.objects.select_related('company').prefetch_related('company__companiesimages_set').get(id = job_id)

            job_info = {
                "position"         : job.position,
                "intro"            : job.intro,
                "main_tasks"       : job.main_tasks,
                "requirements"     : job.requirements,
                "preferred_points" : job.preferred_points,
                "benefits"         : job.benefits,
                "dead_line"        : job.dead_line,
                "job_id"           : job.id
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
                "job"            : job_info,
                "company"        : company_info,
                "company_images" : company_images,
                "tags"           : tags,
                "follow"         : Follows.objects.exists(user_id = user_id, job_id = job_id)
            }

            return JsonResponse(data, status=200)
        except Jobs.NotExist:
            return JsonResponse({"error": "INVALID_JOB_ID"}, status=400)

class JobListView(View) :
    @auth_required
    def get(self, request, category_id) :
        user_id = request.user.id

        if jobs.objects.filter(category_id = category_id).exists():
            job_list = Jobs.objects.filter(category_id=category_id).select_related('company').prefetch_related('tags')
        else:
            job_list = Jobs.objects.all().select_related('company').prefetch_related('tags')

        all_tags = set()
        data     = [] 

        for job in joblist:
            job_info = {
                "position"   : job.position,
                "job_id"     : job.id,
                "dead_line"  : job.dead_line
            }

            company = {
                "company_name"  : job.company.company_name,
                "main_image"    : job.company.main_image,
                "city"          : job.company.city,
                "country"       : job.company.country,
                "company_id"    : job.company.id
            }

            tags     = [{"skill" : tag.skill,"tag_id" : tag.id } for tag in job.tags.all()]
            job_data = {
                "job"      : job_info,
                "company"  : company,
                "tags"     : tags,
                "follow"   : Follows.objects.exists(user_id=user_id, job_id=job.id)
            }
            data.append(job_data)
            all_tags += [tag.skill for tag in job.tags.all()]

        return JsonResponse({"data" : data,"tag_list": list(all_tags)}, status=200)

class FollowedJobView(View) :
    @auth_required
    def get(self, request) :
        follow_list = Follows.objects.filter(user_id=request.user.id).select_related('job').select_related('job__company')

        followed_job_data = [
            job_data = {
                "job" : {
                    "company_name"  : el.job.company.company_name,
                    "main_image"    : el.job.company.main_image,
                    "city"          : el.job.company.city,
                    "country"       : el.job.company.country,
                    "company_id"    : el.job.company.id
                },
                "company" : {
                    "position"  : el.job.position,
                    "job_id"    : el.job.id,
                    "dead_line" : el.job.dead_line
                }
            } for folow_info in follow_list]

        return JsonResponse({"data":followed_job_data}, status=200)
