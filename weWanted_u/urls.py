from django.urls import path, include

urlpatterns = [
    path('users', include('users.urls')),
    path('job', include('job.urls')),
    path('resume', include('resume.urls')),
    path('follow', include('follow.urls')),
    path('repl', include('repl.urls'))
]
