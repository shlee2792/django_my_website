from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', {'posts' : posts,})


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')