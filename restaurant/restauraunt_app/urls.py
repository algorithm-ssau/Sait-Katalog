from django.urls import path
from .views import home, about_us, menu, personal_page, login_page, logout

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_us, name='about_us'),
    path('menu/', menu, name='menu'),
    path('personal/', personal_page, name='personal_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout, name='logout'),
]
