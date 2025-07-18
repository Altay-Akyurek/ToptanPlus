from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    image_url=models.URLField(blank=True)
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    is_populer=models.BooleanField(default=True)
    is_new=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name