from django.db import models # type: ignore

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=150)    
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    end_time = models.DateField()

    def __str__(self):
        return self.name
