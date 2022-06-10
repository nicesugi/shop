from operator import mod
from django.db import models
from user.models import User

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, related_name='categories')
    image = models.CharField(max_length=256)
    desc = models.TextField()
    price = models.CharField(max_length=20)
    store = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
    
class OrderStatus(models.Model):
    ORDER = 'OR'
    PAID = 'PAID'
    CANCEL = 'CC'
    DEPARTURE = 'DEP'
    ARRIVE = 'ARR'
    ORDER_STATUS = (
        (ORDER, 'Order'),
        (PAID, 'Paid'),
        (CANCEL, 'Cancel'),
        (DEPARTURE, 'Departure'),
        (ARRIVE, 'Arrive'),
    )
    status = models.CharField(max_length=4, choices=ORDER_STATUS)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



class ProductOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    # user > ProductOrder / userOrder / OrderStatus / Product / Category 확인가능
    # order > 상품주문>주문상태>상품 
    

class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, default='')
    order_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.time.now)
    price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20)
    fin_count = models.CharField(max_length=20)
    boolean = models.BooleanField()
    


