from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse

def home(request):
    return render(request, 'main_page.html')

def about_us(request):
    return render(request, 'about_us_page.html')

def menu(request):
    return render(request, 'menu.html')

def personal_page(request):
    user_login = request.COOKIES.get('user_login')
    context = {'user_login': user_login}
    return render(request, 'personal_page.html', context)

def login_page(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        login = request.POST.get('login')
        password = request.POST.get('password')

        if action == 'register':
            if User.objects.filter(login=login).exists():
                messages.error(request, 'Пользователь с таким логином уже существует')
            else:
                user = User(login=login)
                user.set_password(password)
                user.save()
                response = redirect('personal_page')
                response.set_cookie('user_login', login)
                return response

        elif action == 'login':
            try:
                user = User.objects.get(login=login)
                if user.check_password(password):
                    response = redirect('personal_page')
                    response.set_cookie('user_login', login)
                    return response
                else:
                    messages.error(request, 'Неверный логин или пароль')
            except User.DoesNotExist:
                messages.error(request, 'Неверный логин или пароль')

    return render(request, 'log_in_page.html')

def logout(request):
    response = redirect('personal_page')
    response.delete_cookie('user_login')
    return response
