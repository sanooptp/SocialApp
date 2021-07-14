from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Post

class FeedsView(ListView):
    template_name= 'feeds/feeds.html'
    model= Post


