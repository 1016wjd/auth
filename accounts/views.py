from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST) # request들어가야함 > 공식문서 확인
        if form.is_valid():
            auth_login(request, form.get_user()) #   위에서 로그인 함수 가져와야 함 

            next_url = request.GET.get('next') # => /articles/create/ (마지막에 있던 위치로 반환)
            
            return redirect(next_url or 'articles:index')
            # next 인자가 url에 있을 때 => '/articles/create/' or 'articles:index'
    else:
        form = CustomAuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

