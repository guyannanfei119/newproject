from django.shortcuts import render, HttpResponse

# Create your views here.

def book(request):
    return  HttpResponse("图书")
