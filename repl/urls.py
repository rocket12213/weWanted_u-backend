from django.urls    import path
from .views         import DropDownView, ReplView

urlpatterns = [
        path('/<int:sort_id>',DropDownView.as_view()),
        path('/repl', ReplView.as_view()), 
]

