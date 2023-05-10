from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50,label='Username')
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30 , label = 'First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Password Confirmation')
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
    
    
    
    
class loginForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')
        
        
        
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50,label='Username')
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30 , label = 'First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email' )
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('image',)
        
        
