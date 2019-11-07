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
        access_token = request.headers.get('Authorization')
        follow_data = json.loads(request.body)

        payload = jwt.decode(access_token, "secret", algorithm="HS256")
        user=Users.objects.get(email=payload["email"])
        job_id = follow_data["job_id"]
        follow = follow_data["follow"]

        if follow :
            Follows.objects.create(user_id=user.id, job_id=job_id)
        elif follow == False :
            Follows.objects.filter(user_id=user.id, job_id=job_id).delete()

        return JsonResponse({"message":follow}, status=200)
