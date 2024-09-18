from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm

# Sphinx docstring impletmentation
def user_login(request):
    """
    Renders the login page.

    :param request (HttpRequest): The HTTP request object.

    Returns:HttpResponse: The rendered response containing the 'authentication/login.html' template.
    
    :rtype: (Html)HttpResponse
    """
    
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Authenticates the user based on submitted credentials.

    :param request (HttpRequest): The HTTP request object.

    Returns: HttpResponseRedirect: Redirects to the login page if authentication fails,
                              or to the 'shop:home' page if successful.
                              
    :rtype: (html)HttpResponse
    """
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse('user_auth:user_login'))
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('shop:home'))

def show_user(request):
    """
    Displays user information.

    :param request (HttpRequest): The HTTP request object.

    Returns:HttpResponse: The rendered response containing the 'authentication/user.html' template
                      with user information.
                      
    :rtype: str
    """
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register(request):
    """
    Handles user registration.

    :param request (HttpRequest): The HTTP request object.

    Returns:HttpResponse: The rendered response containing the 'authentication/register.html' template
                      with the signup form.
                      
    :rtype: HttpResponse(html)
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:home')
    else:
        form = SignupForm()
    return render(request, 'authentication/register.html', {'form': form})

def signout_user(request):
    """
    Logs out the user.

    :parama request (HttpRequest): The HTTP request object.

    Returns:HttpResponseRedirect: Redirects to the 'shop:home' page after logout.
    
    :rtype: HttpResponse(html)
    """
    logout(request)
    return HttpResponseRedirect(reverse('shop:home'))
