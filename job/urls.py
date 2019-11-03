from django.urls    import path
from .views         import JobDetailPageView

urlpatterns = [
        path('/detail/<int:jobs_id>',JobDetailPageView.as_view()),
]

