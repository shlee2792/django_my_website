from django.shortcuts import render
from .models import Post,Category
from django.views.generic import ListView, DetailView

# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', {'posts' : posts,})


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context

class PostDetail(DetailView):
    model = Post
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context

class PostListByCategory(PostList):
    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug = slug,)
        return Post.objects.filter(category=category).order_by('-created')







# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)
#
#     return render(request, 'blog/post_detail.html', {'blog_post' : blog_post})


