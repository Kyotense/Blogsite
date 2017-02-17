from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
#from taggit.models import Tag
from django.views.generic import ListView

class PostViews(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 4
    queryset = Post.objects.all().order_by("-date")

class TagViews(ListView):

    template_name= 'blog/blog.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("slug"))
