from django.urls    import path
from .views         import DropDownView, ReplView

urlpatterns = [
        path('/careers',DropDownView.as_view()),
        path('/moods',DropDownView.as_view()),
        path('', ReplView.as_view()), 
]

