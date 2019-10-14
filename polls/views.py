from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from polls import views
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from polls.form import PostForm
from polls import form
from polls.models import Post
from django.utils import timezone


def post_create(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
      form = PostForm()
      return render(request, 'post/create.html', {'form': form})
  
def post_index(request):
  all = Post.objects.all()
  return render(request,'post/index.html',{'all':all})


def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request,'post_detail.html',{'post':post})


def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
      form = PostForm(request.POST, instance=post)
      if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'post_edit.html', {'form': form})