from django.urls    import path
from .views         import JobDetailPageView, JobsMainPageView

urlpatterns = [
        path('/detail/<int:job_id>',JobDetailPageView.as_view()),
        path('/main/<int:category_id>', JobsMainPageView.as_view()),
]
