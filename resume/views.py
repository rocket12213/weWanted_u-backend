#from django.shortcuts import render
import json
import jwt

from django.http  import JsonResponse
from django.views import View
from users.utils  import auth_required_decorator
from .models      import Portfolio, Resume  

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

    def post(self, request, resume_id):
        resume_data = json.loads(request.body)
        Resume (
            saving_type = resume_data["completed"],
            title       = resume_data["title"], 
            phone       = resume_data["phone"],
            email       = resume_data["email"],
            blog        = resume_data["blog"],
	    about_me    = resume_data["about_me"]
        ).save()
        for single_project in resume_data["projects"] :
            Projects(
                project_title = single_project["project_title"],
                github        = single_project["github"],
		description   = single_project["description"],
		what_did_i_do = single_project["what_did_i_do"],
		tech_stack    = single_project["tech_stack"]
	    ).save()
        return JsonResponse({"message":"수정이 완료되었습니다"}, status=200)
            
class NewResumeView(View):
    @auth_required_decorator
    def post(self, request):
        resume_data = json.loads(request.body)
        Resume (
            saving_type = resume_data["completed"],
            title       = resume_data["title"], 
            phone       = resume_data["phone"],
            email       = resume_data["email"],
            blog        = resume_data["blog"],
	    about_me    = resume_data["about_me"]
        ).save()
        for single_project in resume_data["projects"] :
            Projects(
                project_title = single_project["project_title"],
                github        = single_project["github"],
		description   = single_project["description"],
		what_did_i_do = single_project["what_did_i_do"],
		tech_stack    = single_project["tech_stack"]
	    ).save()
        return JsonResponse({"message":"생성이 완료되었습니다"}, status=200)
            



	
# Create your views here.
