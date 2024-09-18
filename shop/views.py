from django.shortcuts import render
from shop.models import Contact
 
# impletmenting docstrings for each view 
def news_letter(request):
    """
    Renders the 'news_letter.html' template.

    :param request (HttpRequest): The HTTP request object.

    :returns HttpResponse: The rendered response containing the 'news_letter.html' template.
    """
    return render(request, 'news_letter.html')

def subscribe(request):
    """
    Renders the 'subscribe.html' template.

    :param request (HttpRequest): The HTTP request object.

    :returns HttpResponse: The rendered response containing the 'subscribe.html' template.
    """
    return render(request, 'subscribe.html')

def shopnow(request):
    """
    Renders the 'shopnow.html' template.

    :param request (HttpRequest): The HTTP request object.

    :returns HttpResponse: The rendered response containing the 'shopnow.html' template.
    """
    return render(request, 'shopnow.html')

def home(request):
    """
    Renders the 'home.html' template.

    :param request (HttpRequest): The HTTP request object.

    :returns HttpResponse: The rendered response containing the 'home.html' template.
    """
    return render(request, 'home.html')

def contact(request):
    """
    Renders the 'contact.html' template.

    :param request (HttpRequest): The HTTP request object.

    :returns HttpResponse: The rendered response containing the 'contact.html' template.
    """
    return render(request, 'contact.html')

def contact_view(request):
    """
    Handles the contact form submission.

    :param request (HttpRequest): The HTTP request object.

    :returns HttpResponse: The rendered response containing the 'contact_template.html' template
                      (if the form is submitted) or the initial 'contact_template.html' template.
    """
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        country = request.POST['country']
        subject = request.POST['subject']
        print(firstname, lastname, country, subject)
        new_contact = Contact(username=request.user.username, first_name=firstname, last_name=lastname, country=country, subject=subject)
        new_contact.save()
        return render(request, "contact_template.html", {'new_contact': new_contact})
    return render(request, 'contact_template.html')
