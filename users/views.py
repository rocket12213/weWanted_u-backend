import Json
import bcrypt
from django.http import Jsonresponse
from django.views import view


class SignupView(view) :
    def post (self, request) :
        login_data = json.loads(request.body)
        
        try :
            if len(login_data["email"])>20 :
                return JsonResponse({"message":"Too_Long_Email"}, status=400)
            
            if len(login_data["password"])<12 :
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
            return JsonResponse({"message":"Wrong_Path"}, status=403)



class AuthView(view) : 
    def post(self, request) :
        login_data = json.loads(request.body)
        password   = login_data["password"]

        try :
        exist_user = Users.objects.get(email=login_data["email"])
            if bcrypt.checkpw(password.encode("utf-8"), exit_user.password.encode("utf-8")) :
                payload 	  = {"email" : exit_user.id}
		encryption_secret = "secret"
		algorithm	  = "HS256"
		encoded		  = jwt.encode(payload, encryption_secret, algorithm=algorithm)
		return JsonResponse({"JsonWebToken":encoded.decode("UTF-8")}, status=200)
 
        except Users.DoesNotExist :
		return JsonResponse({"message":"INVALID_EMAIL"}, status=400)


# Create your views here.
