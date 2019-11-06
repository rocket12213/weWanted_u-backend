#from django.shortcuts import render
import json
import jwt

from django.http  import JsonResponse
from django.views import View
from users.utils  import auth_required_decorator
from django.db    import transaction
from .models      import Portfolio, Resume, SavingTypes, Projects  

class SavingTypesView(View) :
    @auth_required_decorator
    def get(self, request) :
        resume_data = json.loads(request.body)
        res = list(SavingTypes.objects.filter(saving_type=resume_data["completed"]).values())
        saving_type = json.dumps(res)

        return JsonResponse({"completed":saving_type}, status=200)

class PortfolioView(View):
    @auth_required_decorator
    def get(self, request):
        user = request.exist_user
        res = list(Portfolio.objects.filter(user=user).values())
        portfolio = json.dumps(res)

        return JsonResponse({"portfolio":portfolio}, status=200)	

class SavedResumeView(View): 
    @auth_required_decorator
    def get(self, request, resume_id):
        res = list(Resume.objects.get(pk=["resume_id"]).values())
        written_resume = jason.dumps(res)
        return JsonResponse(written_resume, status=200)	 

    @auth_required_decorator
    @transaction.atomic()
    def post(self, request, resume_id):
        resume_data = json.loads(request.body)
        saving_type = SavingTypes.objects.get(saving_type=resume_data["completed"]) 
        resume = Resume (
            saving_type = saving_type,
            title       = resume_data["title"], 
            phone       = resume_data["phone"],
            email       = resume_data["email"],
            blog        = resume_data["blog"],
	    about_me    = resume_data["about_me"]
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

        return JsonResponse({"message":"수정이 완료되었습니다"}, status=200)
            
class NewResumeView(View):
    @auth_required_decorator
    @transaction.atomic()
    def post(self, request) :
        resume_data = json.loads(request.body)
        saving_type = SavingTypes.objects.get(saving_type=resume_data["completed"]) 
        resume =  Resume (
            saving_type = saving_type,
            title       = resume_data["title"], 
            phone       = resume_data["phone"],
            email       = resume_data["email"],
            blog        = resume_data["blog"],
            about_me    = resume_data["about_me"]
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

        return JsonResponse({"message":"생성이 완료되었습니다"}, status=200)

            



	
