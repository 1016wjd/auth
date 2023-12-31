from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)

@login_required # 로그인을 하지 않으면 실행할 수 없음!
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False) # 유저를 넣을 공간이 없음
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'form.html', context)