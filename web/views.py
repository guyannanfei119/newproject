from django.shortcuts import render, HttpResponse

# Create your views here.

def book(request):
    return  HttpResponse("图书1")

def music(request):
    return  HttpResponse("音乐2")

def video(request):
    return  HttpResponse("视频3")

def xiaoshuo(request):
    return  HttpResponse("小说4")
