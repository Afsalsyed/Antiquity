from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore

products=[
        {'name':'aaa', 'description': 'details abouth the product-a', 'sprice': '1001', 'cprice': '1451'},
        {'name':'bbb', 'description': 'details abouth the product-b', 'sprice': '1002', 'cprice': '1452'},
        {'name':'ccc', 'description': 'details abouth the product-c', 'sprice': '1003', 'cprice': '1453'},
        {'name':'ddd', 'description': 'details abouth the producd-d', 'sprice': '1004', 'cprice': '1454'},
        {'name':'eee', 'description': 'details abouth the product-e', 'sprice': '1005', 'cprice': '1455'},
        {'name':'fff', 'description': 'details abouth the product-f', 'sprice': '1006', 'cprice': '1456'}
    ]

# Create your views here.
def home(request):
    return render(request, 'index.html', {'products': products})

def details(request):
    return render(request, "details.html")