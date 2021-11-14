from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def sign_up(request):
    context = {}

    if request.method == 'POST':
        if (request.POST.get('username') and 
            request.POST.get('password') and 
            request.POST.get('password') == request.POST.get('password_check')):

            # Django 내장 create_user 함수를 이용한다.
            new_user = User.objects.create_user(
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )

            # 로그인처리
            auth.login(request, new_user)
            return redirect('main:main')

        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
    
    return render(request, 'accounts/sign_up.html', context)

def login(request):
    context = {}

    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            
            # authenticate함수를 사용한다., 첫번째 인자는 request
            # db에는 암호화된 password가 저장되기 때문에 직접비교는 불가능 하기때문에 authenticate함수를 이용
            user = auth.authenticate(
                request,
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )

            if user is not None:

                auth.login(request, user)
                return redirect('main:main')
            else:
                context['error'] = "아이디와 비밀번호를 다시 확인해주세요."

        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
    
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        
    return redirect('main:main')