from django.shortcuts import render
from .models import Article

def archive(request):
    posts = Article.objects.all() # Берем все статьи из базы
    return render(request, 'archive.html', {"posts": posts})