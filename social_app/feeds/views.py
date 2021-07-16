from feeds.forms import PostForm
from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm


class FeedsView(ListView):
    template_name= 'feeds/feeds.html'
    model= Post

class AddPostView(CreateView):
    template_name = 'feeds/add_post.html'
    form_class = PostForm
    success_url = reverse_lazy("feeds")

    def post(self, request):
        form = self.form_class(request.POST, request.FILES or None)
        if  request.method == "POST":
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user= request.user
                obj.save()
                return redirect('feeds')
            context = {'form': form}
            return render(request, self.template_name, context)
