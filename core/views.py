from django.shortcuts import render

# Create your views here.

from .models import Core

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'


class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Core
    #fields = ['name']
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('core:posts')

    def form_valid(self, form):
        messages.add_message(
                self.request,
                messages.SUCCESS,
                'The post added successfully'
                )
        return super().form_valid(form)


class EditView(UpdateView):
    model = Core
    #fields = ['name']
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kward = 'pk'
    success_url = reverse_lazy('core:posts')

class Delete(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')
    template_name = "core/confirm-delete.html"
