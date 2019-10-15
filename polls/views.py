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
from django.contrib.postgres.search import SearchVector
from django.contrib import auth, messages
from django.db.models import Q

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
  # paginator = Paginator(post_list, 4)

  try:
    page_number = int(request.GET.get('page', '1'))
  except:
    page_number = 1

  post_result = do_paginate(post_list, page_number)
 
  # try:
  #   # get data list for the specified page_number.
  #   posts = paginator.page(page_number)
  # except PageNotAnInteger:
  #   # if the page_number is not an integer then return the first page data.
  #   posts = paginator.page(1)
  # except EmptyPage:
  #   # get the lat page data if the page_number is bigger than last page number.
  #   posts = paginator.page(paginator.num_pages)
  
  posts = post_result[0]
  paginator = post_result[1]

  base_url = '/post?' 
  return render(request, 'post/index.html',{'post_list': posts, 'paginator' : paginator, 'base_url': base_url})

def do_paginate(data_list, page_number):
    result_per_page = 4
    paginator = Paginator(data_list, result_per_page)

    try:
      # get data list for the specified page_number.
      posts = paginator.page(page_number)
    except PageNotAnInteger:
      # if the page_number is not an integer then return the first page data.
      posts = paginator.page(1)
    except EmptyPage:
      # get the lat page data if the page_number is bigger than last page number.
      posts = paginator.page(paginator.num_pages)
    
    return [posts, paginator]

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

def search(request):
  if request.method == 'GET':
    searched_keyword = request.GET['title']
    
    if searched_keyword:
      post_list = Post.objects.filter(Q(title__icontains=searched_keyword) | Q(email__icontains=searched_keyword))
      if post_list:
        try:
          page_number = int(request.GET.get('page', '1'))

        except:
          page_number = 1
        post_result = do_paginate(post_list, page_number)

        posts = post_result[0]

        paginator = post_result[1]

        base_url = '/post?' 
        return render(request, 'post/index.html',{'post_list': posts, 'paginator' : paginator, 'base_url': base_url, 'searched_keyword': searched_keyword})
        # return render(request,'post/index.html',{'post_list':post_list, })
      else:
        messages.add_message(request,messages.INFO,' No result found ')
    else:
      return redirect('post')
  return render(request,"post/index.html")