from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.http import HttpResponse  # type: ignore
from .models import Product
from .forms import ProductForm
from django.contrib import messages # type: ignore


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def details(request):
    return render(request, "details.html")

def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product posted successfully!')
            return redirect('home')
        else:
            print(form.errors)  # Debug: Print form errors to console
            messages.error(request, 'There was an error in the form.')
    else:
        form = ProductForm()
    return render(request, 'post_product.html', {'form': form})