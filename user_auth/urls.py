from django.contrib.auth import authenticate, login
from . import views
from django.urls import path

app_name = 'user_auth'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('authenticate_user/',views.authenticate_user,name='authenticate_user'), 
    path('profile/',views.show_user,name="show_user"),
    path('login/',views.user_login, name='user_login' ),
    path('logout_user/,',views.signout_user,name="signout"),
    
]

