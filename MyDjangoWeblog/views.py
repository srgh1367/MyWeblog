from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(requset):
    return render(requset, "home.html")


def about(requset):
    return render(requset, "about.html")
