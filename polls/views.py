from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from polls import views
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from polls.form import PostForm, ContactForm
from polls.models import Post


def post_create(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()      
      return redirect('post')   
  else:
      form = PostForm()
      return render(request, 'post/create.html', {'form': form})
  
def post_index(request):
  all = Post.objects.all()
  return render(request,'post/index.html',{'all':all})


def home(request):
  if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
          pass  # does nothing, just trigger the validation
  else:
      form = ContactForm()
  return render(request, 'home.html', {'form': form})