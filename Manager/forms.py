from django import forms
from .models import Fine
from django.contrib.auth.models import User


class FineForm(forms.ModelForm):
    
    class Meta:
        model = Fine
        fields = ("employee_id","employee","fine", "reason")
        
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name")
        
        

     
