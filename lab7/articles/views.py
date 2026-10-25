from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {"posts": posts})

def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {"post": post})

def create_post(request):
    if request.user.is_anonymous:
        raise Http404
    
    if request.method == "POST":
        form = {'text': request.POST.get("text"), 'title': request.POST.get("title")}
        if form["text"] and form["title"]:
            if Article.objects.filter(title=form["title"]).exists():
                form['errors'] = "Статья с таким названием уже существует!"
                return render(request, 'create_post.html', {'form': form})
            
            article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
            return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Проверка на пустые поля
        if not username or not password:
            return render(request, 'register.html', {'error': 'Заполните логин и пароль!'})
            
        # Проверка уникальности логина
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Пользователь с таким логином уже существует!'})
            
        # Создание пользователя
        User.objects.create_user(username, email, password)
        return redirect('user_login')
        
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not username or not password:
            return render(request, 'login.html', {'error': 'Введите логин и пароль!'})
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль!'})
            
    return render(request, 'login.html')