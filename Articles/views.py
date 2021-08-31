from django.shortcuts import render,HttpResponse
from . import models


# Create your views here.
def articles_list(requset):
    articles = models.Article.objects.all().order_by('date')
    args = {'articles': articles}
    return render(requset, "articles/articles_list.html", args)

def articles_detail(requset,slug):
    return HttpResponse(slug)

