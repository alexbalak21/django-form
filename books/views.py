from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView)

from .models import Author


class HomeView(TemplateView):
    template_name = 'home.html'


class AuthorsListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorsCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name', ]

    def form_valid(self, form):

        return super().form_valid(form)
