from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import News, Tag, Author
from .forms import NewsForm


class IndexView(ListView):
    template_name = 'blog/index.html'
    model = News

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = News.objects.order_by('-published')
        return context


class NewsCreateView(CreateView):
    template_name = 'blog/create.html'
    form_class = NewsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()
        return context


class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'description', 'tag']
    success_url = reverse_lazy('index')
    template_name_suffix = '_update'


class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('index')
    template_name_suffix = '_delete'
