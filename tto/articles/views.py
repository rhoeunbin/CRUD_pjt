from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POSt':
        article_form = ArticleForm(request.POST, request) 
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '글 작성 완료')
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form':article_form
    }
    return render(request, 'articles/from.html', context)