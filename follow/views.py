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
        user_id     = request.exist_user.id
        job_id      = json.loads(request.body)["job_id"]
        follow      = json.loads(request.body)["follow"]

        if follow :
            Follows.objects.create(user_id=user_id, job_id=job_id)
        elif follow == False :
            Follows.objects.filter(user_id=user_id, job_id=job_id).delete()

        return JsonResponse({"message":follow}, status=200)
