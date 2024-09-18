from django.db import models
from django.contrib.auth import get_user_model

class Contact(models.Model):
    """
    Represents a contact form submission.

    :param models.Model (object): The model parent class.

    """

    username = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    subject = models.TextField()
    