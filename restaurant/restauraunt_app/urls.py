from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about_us, menu, personal_page, login_page, logout, toggle_favorite

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_us, name='about_us'),
    path('menu/', menu, name='menu'),
    path('personal/', personal_page, name='personal_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout, name='logout'),
    path('toggle-favorite/', toggle_favorite, name='toggle_favorite'),
] 
