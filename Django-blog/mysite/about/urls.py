from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from about.models import AboutUs

urlpatterns = [
    url(r'^$', ListView.as_view(
                        queryset=AboutUs.objects.all(),
                        template_name="about/about.html")),
]
