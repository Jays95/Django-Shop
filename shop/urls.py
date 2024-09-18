
from . import views
from django.contrib import admin
from django.urls import path

app_name = 'shop'
urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('newsletter/',views.news_letter,name='newsletter'),
    path('subscribe/', views.subscribe,name='subscribe'),
    path('shopnow/', views.shopnow, name='shopnow'),
    path('', views.home,name="home"),
]
