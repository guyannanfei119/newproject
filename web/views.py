from django.shortcuts import render, HttpResponse

# Create your views here.

def book(request):
    return  HttpResponse("图书")

def music(request):
    return  HttpResponse("音乐")
