from django.urls import path
from .views import PortfolioView, SavedResumeView, NewResumeView, SavingTypesView

urlpatterns = [
    path('', PortfolioView.as_view()),
    path('/edit/<int:resume_id>', SavedResumeView.as_view()),
    path('/new',NewResumeView.as_view()),
    path('/savingtype', SavingTypesView.as_view()),
]

