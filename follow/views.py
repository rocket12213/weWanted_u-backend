import json
import jwt
from django.http    import JsonResponse
from django.views   import View
from users.models   import Users, Follows
from users.utils    import auth_required_decorator
from job.models     import Jobs

class FollowingView(View) :
    @auth_required_decorator
    def post(self, request) :
        try:
            user_id     = request.user.id
            input_data  = json.loads(request.body)
            job_id      = input_data["job_id"]
            follow      = input_data["follow"]

            if follow:
                Follows.objects.create(user_id=user_id, job_id=job_id)
            else:
                Follows.objects.filter(user_id=user_id, job_id=job_id).delete()

            return JsonResponse({"Followed": follow }, status=200)
        except KeyError:
            ...
        except ConstraintErorr: #정확한 에러 이름은 찾아보세요
            ...
