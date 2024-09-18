from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    """
    Custom form for user registration (signup).

    :param UserCreationForm 
    :type class: the base class   
        first_name (forms.CharField): The user's first name.
        password1 (forms.CharField): The user's chosen password (with validation).
        password2 (forms.CharField): Confirmation of the user's chosen password.
    """

    first_name = forms.CharField(max_length=150, label="First name")

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        """
        Metadata for the SignupForm.

        Attributes:
            model (User): The User model.
            fields (tuple): Fields to include in the form.
        """
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')

    def save(self, commit=True):
        """
        Save the user object after setting the first name.

        :param commit (bool, optional): Whether to save the user immediately. Defaults to True.

        Returns:User: The saved User object.
            
        """
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        if commit:
            user.save()
        return user
