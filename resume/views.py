#from django.shortcuts import render
import json
import jwt

from django.http  import JsonResponse
from django.views import View
from users.utils  import auth_required_decorator
from .models      import My_Portfolio, Resume  

class Show_Portfolio(View):
    @auth_required_decorator
    def get(self, request):
        user = request.exist_user
        print(user)
        my_portfolio = list(My_Portfolio.objects.filter(user=user.id).values())
        return JsonResponse(my_portfolio, safe=False,  status=200)	

class Call_Saved_Resume(View): 
    @auth_required_decorator
    def get(self, request, resume_id):
        written_resume = json.dumps(Resume.objects.get(pk=["resume_id"]))
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
                project_title = each_single_project["project_title"],
                github        = each_single_project["github"],
		description   = each_single_project["description"],
		what_did_i_do = each_single_project["what_did_i_do"],
		tech_stack    = each_single_project["tech_stack"]
	    ).save()
        return JsonResponse({"message":"수정이 완료되었습니다"}, status=200)
            
class Create_New_Resume(View):
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
                project_title = each_single_project["project_title"],
                github        = each_single_project["github"],
		description   = each_single_project["description"],
		what_did_i_do = each_single_project["what_did_i_do"],
		tech_stack    = each_single_project["tech_stack"]
	    ).save()
        return JsonResponse({"message":"생성이 완료되었습니다"}, status=200)
            



	
# Create your views here.
