from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('my-login', views.my_login, name="login"),
    path('main/', views.main, name='main'),

    path('themes/<str:theme>/', views.theme_selection, name='theme_selection'),
        path('themes/', views.themes, name='themes'),
        path('popular/', views.popular, name='popular'),
        path('family/', views.family, name='family'),
        path('school/', views.school, name='school'),
        path('shop/', views.shop, name='shop'),
        path('doctor/', views.doctor, name='doctor'),

    path('difficulty/', views.difficulty, name='difficulty'),
    path('difficulty/<str:level>/', views.difficulty_level, name='difficulty_level'),
    path('sound/', views.sound, name='sound'),
    path('text/', views.text, name='text'),
    path('sentence/', views.sentence, name='sentence'),

]