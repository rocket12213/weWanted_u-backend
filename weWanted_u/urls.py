from django.urls import path, include

urlpatterns = [
    path('company', include('company.urls')),
    path('jobs',    include('jobs.urls')),
]
