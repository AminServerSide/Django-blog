from django.shortcuts import render
from blog.models import Article

def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()[:3]
    return render(request , "home_app/index.html" , {'articles':articles})

def sidebar(request):
    data = {'name' : "amin"}
    return render(request , 'includes/sidebar.html', context=data)
