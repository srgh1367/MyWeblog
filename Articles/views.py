from django.shortcuts import render
from . import models


# Create your views here.
def articles_list(requset):
    articles = models.Article.objects.all().order_by('date')
    args = {'articles': articles}
    return render(requset, "articles/articles_list.html", args)

