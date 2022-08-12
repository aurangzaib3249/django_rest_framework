from dataclasses import fields
import email
from pyexpat import model
from django import forms
from .models import *
from dataclasses import field, fields
from pyexpat import model
from django import forms

from .models import User

from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["full_name",'email','phone_number','address',"password1","password2"]
        widget={
            "full_name":forms.TextInput({"class":"form-control","placeholder":"Enter Full Name"}),
            "email":forms.TextInput({"class":"form-control","placeholder":"E-mail"}),
            "phone_number":forms.TextInput({"class":"form-control","placeholder":"Phone Number"}),
            "password1":forms.PasswordInput({"class":"form-control","placeholder":"Password"}),
            "password2":forms.PasswordInput({"class":"form-control","placeholder":"Confirm Password"}),
            "address":forms.Textarea({"class":"form-control","placeholder":"Full adddres"}),
            
        }
  