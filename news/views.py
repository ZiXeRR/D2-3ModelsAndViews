from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


def news_list(request):
    news = Post.objects.all().order_by('-rating')[:6]
    return render(request, 'news/default.html', context={'news':news})


def detail(request, slug):
    new = Post.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'new:':new})
