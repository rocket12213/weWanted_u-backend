from django.urls    import path
from .views         import RecruitmentView, JobListView

urlpatterns = [
        path('/recruitment/<int:job_id>',RecruitmentView.as_view()),
        path('/list/<int:category_id>', JobListView.as_view()),
]
