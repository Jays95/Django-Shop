
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import authenticate,login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
    path('auth/', include("user_auth.urls")),
    path('', include("shop.urls")),

]

