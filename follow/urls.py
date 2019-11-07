from django.urls    import path
from .views         import FollowingView

urlpatterns = [
        path('', FollowingView.as_view()),
]

