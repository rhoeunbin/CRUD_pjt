from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
#회원정보수정
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
#비밀번호 수정
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# 비밀번호 수정 세션 무효화
from django.contrib.auth import get_user_model, update_session_auth_hash

# Create your views here.
def main(request):
    return render(request, 'accounts/main.html')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:main')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('accounts:main')
        else:
            form = AuthenticationForm()

        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('accounts:index')

def logout(request):
    auth_logout(request)
    return redirect('accounts:main')

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form':form
        }
    
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
		'form': form,
	}
    return render(request, 'accounts/change_password.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 👇👇 세션 무효화 방지를 위해 새로 추가된 코드
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
		'form': form,
	}
    return render(request, 'accounts/change_password.html', context)

#회원 탈퇴
@login_required
def delete(request):
    request.user.delete() # 선 탈퇴
    auth_logout(request)  # 후 로그아웃
    return redirect('articles:index')