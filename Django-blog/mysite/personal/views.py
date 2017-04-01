from django.shortcuts import render
from django.template import Context, Template
from about.models import AboutUs


def index(request):
    return render(request, 'personal/home.html')
