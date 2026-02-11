from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutView.as_view()),
    path('projects/', ProjectsView.as_view()),
    path('contact/', ContactView.as_view()),
]