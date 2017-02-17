from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.views import PostViews, TagViews

urlpatterns = [
                url(r'^$', PostViews.as_view()),
                url(r'^tag/(?P<slug>[-\w]+)/$', TagViews.as_view(), name='tagged'),

                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                    template_name= 'blog/post.html')),
            ]
