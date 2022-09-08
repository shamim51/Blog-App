from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post


# Create your views here.

context = {
    'Post': Post.objects.all()
}
def home(request):
    #return HttpResponse('<h1>Blog home</h1>')
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    #return HttpResponse('<h1>About page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})









"""posts = [
    {
        'author': 'shamim',
        'title': 'Blog post 1',
        'content': 'first post',
        'date_posted': 'sep 4, 2022'
    },
    {
        'author': 'rony',
        'title': 'Blog post 2',
        'content': 'second post',
        'date_posted': 'sep 5, 2022'
    },
    {
        'author': 'akash',
        'title': 'Blog post 3',
        'content': 'third post',
        'date_posted': 'sep 6, 2022'
    },
    {
        'author': 'arif',
        'title': 'Blog post 4',
        'content': 'fourth post',
        'date_posted': 'sep 7, 2022'
    }
]"""
