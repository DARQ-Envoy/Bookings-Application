from django.forms import ModelForm
from django.contrib.auth.models import User as Business
from django import forms


class User_Login_Form(ModelForm):
    class Meta:
        model = Business
        fields = ["username", "password"]
        widgets= {
            "password": forms.PasswordInput()
        }



class User_Signup_Form(ModelForm):
    class Meta:
        model = Business
        fields = ["first_name", "last_name", "username", "password"]
        widgets= {
            "password": forms.PasswordInput()
        }