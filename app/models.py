from django.db import models # type: ignore
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)    
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    end_time = models.DateField()

    def __str__(self):
        return self.name

class Bid(models.Model):
    product = models.ForeignKey(Product, related_name='bids', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} - {self.bid_price}'