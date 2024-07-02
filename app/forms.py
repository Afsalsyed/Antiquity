from django import forms # type: ignore
from .models import Product, Bid

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