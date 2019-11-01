from django.urls import path
from .views      import SignupView, AuthView 

urlpatterns = [
    path('', SignupView.as_view()),
    path('/auth', AuthView.as_view())
]

