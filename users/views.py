import jwt
import json
import bcrypt

from django.http     import JsonResponse
from django.views    import View
from users.models    import Users


class SignupView(View) :
    def post (self, request) :
        login_data = json.loads(request.body)
        
        try :
            if len(login_data["email"]) > 40 :
                return JsonResponse({"message":"TOO_LONG_EMAIL"}, status=400)
            
            if len(login_data["password"]) < 12 :
                return JsonResponse({"message":"Too_Short_Password"}, status=400)

            if Users.objects.filter(email=login_data["email"]).exists() :
                return JsonResponse({"message":"User_Exists"}, status= 400)
            else:
                hased_user_pw = bcrypt.hashpw(login_data["password"].encode("UTF-8"), bcrypt.gensalt())
                Users(
                    email   = login_data["email"],
                    password= hased_user_pw.decode("UTF-8")
                ).save()
                return JsonResponse({"message":"Success"}, status=200)
        except KeyError :
            return JsonResponse({"message":"INVALID_INPUT"}, status=400)

class AuthView(View) : 
    def post(self, request) :
        login_data = json.loads(request.body)
        password   = login_data["password"]

        try :
            exist_user = Users.objects.get(email=login_data["email"])

            if bcrypt.checkpw(password.encode("utf-8"), exist_user.password.encode("utf-8")) :
                payload           = {"id" : exist_user.id}
                encryption_secret = "secret"
                algorithm         = "HS256"
                encoded           = jwt.encode(payload, encryption_secret, algorithm = algorithm)
                return JsonResponse({"acces_token":encoded.decode("UTF-8")}, status=200)
            else : 
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=400)
        except Users.DoesNotExist :
            return JsonResponse({"message":"INVALID_EMAIL"}, status=400)
        except KeyError :
            return JsonResponse({"message":"INVALID_INPUT"}, status=400)



