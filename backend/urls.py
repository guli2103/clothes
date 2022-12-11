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
    path('post-elements/', PostelView.as_view()),
    path('privacy-policy/', PrivacyView.as_view()),
    path('terms-conditions/', TermsView.as_view()),
    path('index-full/', Indexfl.as_view()),
    path('index-full-left/', Indexfr.as_view()),
    path('index-full-right/', Indexfull.as_view()),
    path('index-list-left/', Indexll.as_view()),
   
]