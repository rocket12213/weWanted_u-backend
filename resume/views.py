import json
import jwt

from django.http  import JsonResponse
from django.views import View
from users.utils  import auth_required_decorator
from django.db    import transaction
from .models      import Resume, SavingTypes, Projects  

class SavingTypesView(View) :
    @auth_required_decorator
    def get(self, request) :
       res = list(SavingTypes.objects.values())

       return JsonResponse({"saving_type":res}, status=200)

class ResumeView(View):
    @auth_required
    def get(self, request):
        res = [{
                'id'          : props['id'],
                'user_id'     : props['user_id'],
                'title'       : props['title'],
                'about_me'    : props['about_me'],
                'blog'        : props['blog'],
                'email'       : props['email'],
                'phone'       : props['phone'],
                'saving_type' : props['saving_type_id'],
                'projects'    : [{
                       'resume_id'     : project['resume_id'],
                       'project_title' : project['project_title'],
                       'github'        : project['github'],
                       'description'   : project['description'],
                       'what_did_i_do' : project['what_did_i_do'],
                       'tech_stack'    : project['tech_stack']
                } for project in Projects.objects.filter(resume_id=props['id']).values()],
                'created_at'  : props['created_at'],
                'updated_at'  : props['updated_at']  
        } for props in Resume.objects.filter(user = request.user).values()]

        return JsonResponse({"resume_list":res}, status=200)	

    @auth_required_decorator
    @transaction.atomic()
    def post(self, request) :
        resume_data = json.loads(request.body)
        saving_type = SavingTypes.objects.get(id = resume_data["saving_type_id"])
        resume      = Resume(
            saving_type = saving_type,
            title       = resume_data["title"], 
            phone       = resume_data["phone"],
            email       = resume_data["email"],
            blog        = resume_data["blog"],
            about_me    = resume_data["about_me"],
            user        = request.user
        )
        resume.save()
        
        for single_project in resume_data["projects"] :
            Projects(
                resume        = resume,
                project_title = single_project["project_title"],
                github        = single_project["github"],
                description   = single_project["description"],
                what_did_i_do = single_project["what_did_i_do"],
                tech_stack    = single_project["tech_stack"]
            ).save()
       
        return HttpResponse(status=200)
        
class ResumeUpdateView(View): 
    @auth_required
    def get(self, request, resume_id):
        res = [{
                'id'          : props['id'],
                'title'       : props['title'],
                'about_me'    : props['about_me'],
                'blog'        : props['blog'],
                'email'       : props['email'],
                'phone'       : props['phone'],
                'saving_type' : props['saving_type_id'],
                'projects'    : [{
                                    'resume_id'     : project['resume_id'],
                                    'project_title' : project['project_title'],
                                    'github'        : project['github'],
                                    'description'   : project['description'],
                                    'what_did_i_do' : project['what_did_i_do'],
                                    'tech_stack'    : project['tech_stack']
                                } for project in Projects.objects.filter(resume_id=props['id']).values()],
                'created_at'  : props['created_at'],
                'updated_at'  : props['updated_at']
        } for props in Resume.objects.filter(pk=resume_id).values()]
        
        return JsonResponse({"resume":res}, status=200)	 

    @auth_required_decorator
    @transaction.atomic()
    def post(self, request, resume_id):
        resume_data = json.loads(request.body)
   
        try:
            if Resume.objects.get(pk=resume_id).user == request.user :
                saving_type = SavingTypes.objects.get(id=resume_data["saving_type_id"])

                resume = Resume.objects.filter(pk=resume_id).update(
                    saving_type = saving_type,
                    title       = resume_data["title"], 
                    phone       = resume_data["phone"],
                    email       = resume_data["email"],
                    blog        = resume_data["blog"],
                    about_me    = resume_data["about_me"],
                    user        = request.exist_user,
                ) 

                Project.objects.filter(resume_id=resume_id).delete()
                project = [Projects(
                    resume        = Resume.objects.get(pk=resume_id),
                    project_title = single_project["project_title"],
                    github        = single_project["github"],
                    description   = single_project["description"],
                    what_did_i_do = single_project["what_did_i_do"],
                    tech_stack    = single_project["tech_stack"]
                ) for single_project in resume_data["projects"]]

                Project.objects.bulk_create(projects)

                return HttpResponse(status=200)
            else:
                return JsonResponse({"message":"INVALID_USER"}, status=403) 
        except Resume.DoesNotExist:
            ...
        except KeyError:
            ....
