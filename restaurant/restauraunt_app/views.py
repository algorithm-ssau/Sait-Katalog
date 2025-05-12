from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Dish, FavoriteDish
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'main_page.html')

def about_us(request):
    return render(request, 'about_us_page.html')

def menu(request):
    dishes = Dish.objects.all()
    user = None
    favorite_dish_ids = []
    
    if request.COOKIES.get('user_login'):
        user = get_object_or_404(User, login=request.COOKIES.get('user_login'))
        favorite_dish_ids = list(FavoriteDish.objects.filter(user=user).values_list('dish_id', flat=True))
    
    return render(request, 'menu.html', {
        'dishes': dishes,
        'user': user,
        'favorite_dish_ids': favorite_dish_ids
    })

def personal_page(request):
    user_login = request.COOKIES.get('user_login')
    if not user_login:
        return redirect('login_page')
    
    user = get_object_or_404(User, login=user_login)
    favorite_dishes = Dish.objects.filter(favoritedish__user=user)
    
    return render(request, 'personal_page.html', {
        'user_login': user_login,
        'favorite_dishes': favorite_dishes,
        'user': user
    })

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

def toggle_favorite(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish_id')
        user_login = request.COOKIES.get('user_login')
        
        if not user_login:
            return JsonResponse({'error': 'Пользователь не авторизован'}, status=401)
        
        user = get_object_or_404(User, login=user_login)
        dish = get_object_or_404(Dish, id=dish_id)
        
        favorite, created = FavoriteDish.objects.get_or_create(user=user, dish=dish)
        
        if not created:
            favorite.delete()
            return JsonResponse({'status': 'removed'})
        
        return JsonResponse({'status': 'added'})
    
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)
