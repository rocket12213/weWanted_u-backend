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
#    @transaction.atomic()
    def post(self, request) :
        repl_data = json.loads(request.body)
        repl = Reviews(
                        question        = repl_data["question"],
                        answer          = repl_data["answer"],
                        review          = repl_data["review"],
                        category_id     = repl_data["category_id"],
                        career_id       = repl_data["career_id"],
                        mood_id         = repl_data["mood_id"],
                        route           = repl_data["route_id"],
                        test_level      = repl_data["test_level_id"],
                        result          = repl_data["result_id"],
                        user_id         = request.exist_user.id
        )
        repl.save()

        return JsonResponse({"repl":repl}, status=200)
