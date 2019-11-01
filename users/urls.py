from django.urls import path, include
from .views      import SignupView, AuthView 

urlpatterns = [
    path('', SignupView.as_View()),
    path('', AuthView.as_View())
]

