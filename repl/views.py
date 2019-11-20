import json

from users.utils    import auth_required_decorator
from django.http    import JsonResponse
from django.views   import View
from users.models   import Users
from job.models     import Categories
from company.models import Companies
from repl.models    import Careers, Moods, Routes, TestLevels, Results, Reviews


class ModdeView(View):
    def get(self, request):
        return JsonResponse({"mood": list(Moods.objects.values())},status=200)

class DropDownView(View) :
    def get(self, request,sort_id) :
        if sort_id == 1 :
            category = list(Categories.objects.values())
            return JsonResponse({"category":category}, status=200)
        elif sort_id == 2 :
            career = list(Careers.objects.values())
            return JsonResponse({"career":career},status=200)
        elif sort_id == 3 :
        elif sort_id == 4 :
            route = list(Routes.objects.values())
            return JsonResponse({"route":route},status=200)
        elif sort_id == 5 :
            test_level = list(TestLevels.objects.values())
            return JsonResponse({"test_level":test_level},status=200)
        elif sort_id == 6 :
            result = list(Results.objects.values())
            return JsonResponse({"result":result},status=200)

class ReplyView(View) :
    @auth_required
    def post(self, request) :
        reply_data = json.loads(request.body)
      
        Reviews(
            question      = reply_data["question"],
            answer        = reply_data["answer"],
            review        = reply_data["review"],
            category_id   = reply_data["category_id"],
            career_id     = reply_data["career_id"],
            mood_id       = reply_data["mood_id"],
            route_id      = reply_data["route_id"],
            test_level_id = reply_data["test_level_id"],
            result_id     = reply_data["result_id"],
            user_id       = request.user.id,
            company_id    = reply_data["company_id"]
        ).save()

        return JsonResponse({"data": {
            "question" : reply_data["question"],
            "answer"   : reply_data["answer"],
            "review"   : reply_data["review"]
        }}, status=200)

