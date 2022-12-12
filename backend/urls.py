from django.urls import path
from .views import *
from backend.views import *

urlpatterns = [
    path('', home),
    path('about/', AboutView.as_view(), name = "about"),
    path('contact/', ContactView.as_view(), name= 'contact'),
    path('author/', AuthorView.as_view(), name='author'),
    path('post-details-1/', Post1View.as_view(), name='post-details-1'),
    path('post-details-2/', Post2View.as_view(), name='post-details-2'),
    path('post-elements/', PostelView.as_view(), name='post-elements'),
    path('privacy-policy/', PrivacyView.as_view(), name='privacy-policy'),
    path('terms-conditions/', TermsView.as_view(), name='terms-conditions'),
    path('index-full/', Indexfl.as_view(), name='index-full'),
    path('index-full-left/', Indexfr.as_view(), name='index-full-left'),
    path('index-full-right/', Indexfull.as_view(), name='index-full-right'),
    path('index-list-left/', Indexll.as_view(), name='index-list-left'),
    path('index-list-right/', Indexlr.as_view(), name='index-list-right'),
    path('index-list/', Indexlist.as_view(), name='index-list'),
]