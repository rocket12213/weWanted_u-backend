import json
import jwt

from django.http   import JsonResponse
from users.models  import Users
from django.views  import View

def auth_required_decorator(func) :

    def wrapper(self, request, *args, **kwargs) :

        if "Authorization" not in request.headers :
            return JsonResponse({"message" : "INVALID_TRIAL"}, status=401)
      
        encoded_access_token = request.headers["Authorization"]
        try :
             decoded_access_token = jwt.decode(encoded_access_token, "secret",  algorithm="HS256")
            
             exist_user = Users.objects.get(id=decoded_access_token["email"])
             request.exist_user = exist_user
             return func(self, request, *args, **kwargs)
        
        except jwt.DecodeError : 
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 401)
        
        except Users.DoesNotExist :
            return JsonResponse({"message" : "UNKNOWN_USER"}, status = 401)
		
    return wrapper

