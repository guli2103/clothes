from django.urls import path
from .views import *
from backend.views import *

urlpatterns = [
    path('', home),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('author/', AuthorView.as_view()),
    path('post-details-1/', Post1View.as_view()),
    path('post-details-2/', Post2View.as_view()),
]