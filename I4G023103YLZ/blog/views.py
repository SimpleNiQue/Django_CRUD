
#* Django imports
from django.shortcuts import render 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
#====================================================

# My imports
from .models import Post
#============================================

class PostListView(ListView):
  class Meta:
    model = Post

  def get_queryset(self):
      return Post.objects.order_by('id')


class PostCreateView(CreateView):
  class Meta:
    model = Post
    form_class = None #! Create a form later and call it here
    fields = ['__all__',]
    success_url = reverse_lazy('blog:all')

  def get_queryset(self):
      return Post.objects.all()


class PostDetailView(DetailView):
  class Meta:
    model = Post
    fields = '__all__'

  def get_queryset(self):
      return Post.objects.order_by('id')


class PostUpdateView(UpdateView):
  class Meta:
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')

  def get_queryset(self):
      return Post.objects.order_by('id')


class PostDeleteView(DeleteView):
  class Meta:
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')

  def get_queryset(self):
      return Post.objects.order_by('id')