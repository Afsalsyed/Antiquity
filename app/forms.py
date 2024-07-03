from django import forms # type: ignore
from .models import Product, Bid
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore

class ProductForm(forms.ModelForm):
    end_time = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Ensure this matches the format users will input
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD',
            'type': 'date'  # This will use the browser's date picker
        })
    )


    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'starting_price', 'end_time']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_price']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))