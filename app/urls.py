from django.urls import path

from . import views

urlpatterns = [
    path('',views.personal_cv),
    path('projects/',views.projects)
]