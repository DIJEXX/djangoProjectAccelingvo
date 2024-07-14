from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('my-login', views.my_login, name="login"),
    path('main/', views.main, name='main'),

    path('themes/', views.themes, name='themes'),
        path('popular/', views.popular, name='popular'),
        path('family/', views.family, name='family'),
        path('school/', views.school, name='school'),
        path('shop/', views.shop, name='shop'),
        path('doctor/', views.doctor, name='doctor'),

    path('dictionary/', views.dictionary, name='dictionary'),
    path('easy/', views.easy, name='easy'),
    path('medium/', views.medium, name='medium'),
    path('hard/', views.hard, name='hard'),

    path('sound/', views.sound, name='sound'),
    path('text/', views.text, name='text'),
    path('sentence/', views.sentence, name='sentence'),

]