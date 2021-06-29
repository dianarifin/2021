from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author' : 'dian',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'Ynita',
        'title' : 'blog post 2',
        'content' : 'Second post content',
        'date_posted' : 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})

 