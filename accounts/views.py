from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')
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
            return redirect('accounts:login')
    else:
        form = CustomAuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)
