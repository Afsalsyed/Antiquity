from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.http import HttpResponse  # type: ignore
from .models import Product
from .forms import ProductForm
from django.contrib import messages # type: ignore

# products=[
#         {'name':'aaa', 'description': 'details abouth the product-a', 'sprice': '1001', 'cprice': '1451'},
#         {'name':'bbb', 'description': 'details abouth the product-b', 'sprice': '1002', 'cprice': '1452'},
#         {'name':'ccc', 'description': 'details abouth the product-c', 'sprice': '1003', 'cprice': '1453'},
#         {'name':'ddd', 'description': 'details abouth the producd-d', 'sprice': '1004', 'cprice': '1454'},
#         {'name':'eee', 'description': 'details abouth the product-e', 'sprice': '1005', 'cprice': '1455'},
#         {'name':'fff', 'description': 'details abouth the product-f', 'sprice': '1006', 'cprice': '1456'}
#     ]

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