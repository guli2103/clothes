from django.shortcuts import render
from .models import *
from django.views.generic import *

def home(request):
    posts = Post.objects.all()
    tposts = TopPost.objects.all()
    mposts = MainPost.objects.all()
    cposts = CatePost.objects.all()
    lposts = LatPost.objects.all()
    context = {
        'posts' : posts,
        'tposts' : tposts,
        'mposts' : mposts,
        'cposts' : cposts,
        'lposts' : lposts,
    }
    return render(request, 'index.html', context)


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'


class AuthorView(TemplateView):
    template_name = 'author.html' 

class Post1View(TemplateView):
    template_name = 'post-details-1.html'

class Post2View(TemplateView):
    template_name = 'post-details-2.html'           




