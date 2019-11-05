from django.urls import path
from .views import Show_Portfolio, Call_Saved_Resume, Create_New_Resume

urlpatterns = [
    path('', Show_Portfolio.as_view()),
    path('preview/<int:resume_id>', Call_Saved_Resume.as_view()),
    path('edit/<int:resume_id>', Create_New_Resume.as_view())
    ]


