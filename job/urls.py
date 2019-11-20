from django.urls    import path
from .views         import RecruitmentView, JobListView, FollowedJobView

urlpatterns = [
        path('/<int:job_id>',RecruitmentView.as_view()),
        path('/category/<int:category_id>', JobListView.as_view()),
        path('/my_account',FollowedJobView.as_view())
]
