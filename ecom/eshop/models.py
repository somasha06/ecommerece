from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.FloatField(default=0.0)
    discount_price=models.FloatField(default=None)
    image=models.ImageField(upload_to="productimage/")
    description=models.TextField()

    def __str__(self):
        return self.title
