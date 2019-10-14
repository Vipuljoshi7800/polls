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
from django.core.paginator import Paginator
from django.contrib.auth.models import User

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
  post_list = Post.objects.all()
  paginator = Paginator(post_list, 4)
  
  try:
    page_number = int(request.GET.get('page', '1'))
  except:
    page_number = 1
  
  try:
    # get data list for the specified page_number.
    posts = paginator.page(page_number)
  except PageNotAnInteger:
    # if the page_number is not an integer then return the first page data.
    posts = paginator.page(1)
  except EmptyPage:
    # get the lat page data if the page_number is bigger than last page number.
    posts = paginator.page(paginator.num_pages)

  base_url = '/post?' 
  return render(request, 'post/index.html', {'post_list': posts, 'paginator' : paginator, 'base_url': base_url})

  # contacts = paginator.get_page(page)
  # return render(request, 'post/index.html', {'contacts': contacts})

  # page_number = request.GET.get('page', 3)
  # page = request.Ge
  # paginate_result = Paginator(user_list, page_number)
  # user_list = paginate_result(1)
  # paginator = paginate_result(4)
   
  # return render(request, 'post/index.html',{'user_list': user_list, 'paginator' : paginator})
 
  # all = Post.objects.all()
  # return render(request,'post/index.html',{'all':all})

def do_paginate(data_list, page_number):
    ret_data_list = data_list
    # suppose we display at most 2 records in each page.
    result_per_page = 2
    # build the paginator object.
    paginator = Paginator(data_list, result_per_page)
    try:
        # get data list for the specified page_number.
        ret_data_list = paginator.page(page_number)
    except EmptyPage:
        # get the lat page data if the page_number is bigger than last page number.
        ret_data_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # if the page_number is not an integer then return the first page data.
        ret_data_list = paginator.page(1)
    return [ret_data_list, paginator]

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

