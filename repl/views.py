import json
from users.utils    import auth_required_decorator
from django.http    import JsonResponse
from django.views   import View
from users.models   import Users
from job.models     import Categories
from company.models import Companies
from repl.models    import Careers, Moods, Routes, TestLevels, Results, Reviews

class DropDownView(View) :
    def get(self, request,sort_id) :
        if sort_id == 1 :
            category = list(Categories.objects.values())
            return JsonResponse({"category":category}, status=200)
        elif sort_id == 2 :
            career = list(Careers.objects.values())
            return JsonResponse({"career":career},status=200)
        elif sort_id == 3 :
            mood = list(Moods.objects.values())
            return JsonResponse({"mood":mood},status=200)
        elif sort_id == 4 :
            route = list(Routes.objects.values())
            return JsonResponse({"route":route},status=200)
        elif sort_id == 5 :
            test_level = list(TestLevels.objects.values())
            return JsonResponse({"test_level":test_level},status=200)
        elif sort_id == 6 :
            result = list(Results.objects.values())
            return JsonResponse({"result":result},status=200)

class ReplView(View) :
    @auth_required_decorator
    def post(self, request) :
        repl_data       = json.loads(request.body)
        category        = repl_data["category"]
        career          = repl_data["career"]
        mood            = repl_data["mood"]
        route           = repl_data["route"]
        test_level      = repl_data["test_level"]
        result          = repl_data["result"]
        company_name    = repl_data["company_name"]
        user            = request.exist_user.id

        category_id     = Categories.objects.get(category=category).id
        career_id       = Careers.objects.get(career=career).id
        mood_id         = Moods.objects.get(mood=mood).id
        route_id        = Routes.objects.get(route=route).id
        test_level_id   = TestLevels.objects.get(level=test_level).id
        result_id       = Results.objects.get(result=result).id
        company_id      = Companies.objects.get(company_name=company_name).id
        
        repl = Reviews(
                        question            = repl_data["question"],
                        answer              = repl_data["answer"],
                        review              = repl_data["review"],
                        category_id         = category_id,
                        career_id           = career_id,
                        mood_id             = mood_id,
                        route_id            = route_id,
                        test_level_id       = test_level_id,
                        result_id           = result_id,
                        user_id             = request.exist_user.id,
                        company_id          = company_id
        )
        repl.save()
        data = {
                "question" : repl_data["question"],
                "answer"   : repl_data["answer"],
                "review"    : repl_data["review"]
                }
        #re = Reviews.objects.select_related('company').select_related('category').select_related('career').select_related('mood').select_related('route').select_related('test_level').select_related('result').filter(user_id=
#        result_data = {
#                "question" : Reviews.objects.get(
        

#        review = list(Reviews.objects.valuea()
        
        return JsonResponse({"data":data}, status=200)
