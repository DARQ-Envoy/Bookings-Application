from django.db import models
from django.contrib.auth.models import User as Business
# Create your models here.




class Customer(models.Model):
    business = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=300, verbose_name="username") 
    email = models.EmailField(max_length=200, verbose_name="Email address", unique=True)
    password = models.CharField(max_length=200, verbose_name="customer password")
    def __str__(self):
        return f"{self.email}"



class Table(models.Model):
    no = models.CharField(max_length=10,verbose_name="Table number")
    seating_capacity = models.CharField(max_length=100, verbose_name="seating capacity")
    is_booked = models.BooleanField(verbose_name="is table booked", default=False)
    price = models.CharField(max_length=500, verbose_name="Table price")
    description = models.TextField(null=True, blank=True)



    def __str__(self):
        return f"Table {self.no}"



class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservee = models.ForeignKey(Business, on_delete=models.Case, related_name="booking_reservee")
    reservor = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="customer")