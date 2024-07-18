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
        path('travel/', views.travel, name='travel'),

    path('dictionary/', views.dictionary, name='dictionary'),
        path('easy/', views.easy, name='easy'),
        path('medium/', views.medium, name='medium'),
        path('hard/', views.hard, name='hard'),

    path('my_sound/', views.my_sound, name='sound'),
    path('sentence/', views.sentence, name='sentence'),
    path('show_cards', views.show_cards, name='show_cards'),

]