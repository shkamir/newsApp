from django.forms import ModelForm
from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class ContactForm(ModelForm):
    name = forms.CharField(
        label="name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder": "Type in Your Name"},
        ),
        required=True,
    )
    email = forms.EmailField(
        label="email",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={"class":"form-control", "placeholder": "Enter Your Valid Email Address"}
        ),
        required=True,
    )
    message = forms.CharField(
        label="email",
        label_suffix="",
        widget=forms.Textarea(
            attrs={"class":"form-control", "placeholder": "Enter Your Message"}
        ),
        required=True,
    )
    file = forms.FileField(
        label="file",
        label_suffix="",
        widget=forms.FileInput(
            attrs={"class":"form-control-file"}
        ),
        required=False,
    )


    class Meta:
        model = Contact
        fields = "__all__"

class RegisterForm(UserCreationForm):
    """ registering user """
    username = forms.CharField(
        label="Username ",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder": "Type in Your User name"},
        ),
        required=True,
    )
    first_name = forms.CharField(
        label="Full name ",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder": "Type in Your Full name "},
        ),
        required=True,
    )
    email = forms.EmailField(
              label="Email ",
              label_suffix="",
              widget=forms.EmailInput(
                    attrs={"class":"form-control", "placeholder": "Enter your Email Address "},
              ),
              required=True,
              )
    password1 = forms.CharField(
            label="Password ",
            label_suffix="",
            max_length=32,
            widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Type your desired Password"}),
            required=True,
            )
    password2 = forms.CharField(
        label="Confirm Password ",
        label_suffix="",
        max_length=32,
        widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Confirm your Password"}),
        required=True,
        )
    class Meta:
        model = User
        fields = (
            "username",  # form user name
            "first_name",  # for first name
            "email",  # for email
            "password1",  # for password
            "password2",  # for password confirm
        )
        help_texts = {
            "username": None,
        }
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")
        