from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from games.models import VideoGame

urlpatterns = [
    url(r'^$', ListView.as_view(
                        queryset=VideoGame.objects.all(),
                        template_name="games/games.html")),
]
