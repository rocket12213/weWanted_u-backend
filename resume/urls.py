from django.urls import path
from .views import PortfolioView, SavedResumeView, NewResumeView

urlpatterns = [
    path('', PortfolioView.as_view()),
    path('preview/<int:resume_id>', SavedResumeView.as_view()),
    path('edit/<int:resume_id>', NewResumeView.as_view())
]


