from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.http import HttpResponse  # type: ignore
from .models import Product, Bid
from .forms import ProductForm, BidForm
from django.contrib import messages # type: ignore


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    bids = product.bids.all()
    last_bid = bids.order_by('-created_at').first() if bids.exists() else None

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            new_bid = form.cleaned_data['bid_price']
            if (last_bid and new_bid <= last_bid.bid_price) or new_bid <= product.starting_price:
                messages.error(request, 'The new bid must be higher than the last bid and the starting price.')
            else:
                bid = form.save(commit=False)
                bid.product = product
                bid.user = request.user
                bid.save()
                messages.success(request, 'Bid placed successfully!')
                return redirect('details', pk=product.pk)
        else:
            messages.error(request, 'There was an error in your bid.')
    else:
        form = BidForm()
    return render(request, 'details.html', {'product': product, 'bids': bids, 'form': form, 'last_bid': last_bid})
    

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
            messages.error(request, 'There was an error in the form.')
    else:
        form = ProductForm()
    return render(request, 'post_product.html', {'form': form})