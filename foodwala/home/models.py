from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel

# Create your models here.

class Category(models.Model):

    cat_name = models.CharField(max_length=100)
    cat_img = models.ImageField(upload_to='catimg/')

    def __str__(self):
        return self.cat_name


class Food(models.Model):
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods', verbose_name='Food Category')
    food_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    food_img = models.ImageField(upload_to='foodimg/')

    class Meta:
        ordering = ['cat_name']

    def __str__(self):
        return self.food_name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.user.first_name
    


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.PositiveIntegerField(default=1)
    mobile = models.CharField(max_length=100)
    address = models.TextField()
    usermail = models.EmailField()

    def __str__(self):
        return self.usermail