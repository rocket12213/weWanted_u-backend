from django.urls    import path
from .views         import JobDetailPageView, JobsMainPageView

urlpatterns = [
        path('/detail/<int:categories_id>/<int:jobs_id>', JobDetailPageView.as_view()),
        path('/main/<int:categories_id>', JobsMainPageView.as_view()),
]
