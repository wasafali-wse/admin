from django.db import models
from django.utils import timezone
import psycopg2
from django.contrib.auth.models import User
class Customer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Token(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return f"Token for {self.customer.name} on {self.date}"

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('Token', 'Token'),
        ('Checking', 'Checking'),
        ('Pending', 'Pending'),
        ('Repairing', 'Repairing'),
        ('Return', 'Return'),
        ('Received', 'Received'),
        ('OK', 'OK'),
        ('NEW', 'NEW'),
        ('USED', 'USED'),
        ('Claim', 'Claim'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    qty = models.IntegerField()
    item = models.CharField(max_length=100)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    advance = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


    def __str__(self):
        return f"Invoice {self.id} for {self.customer.name}"


class Vendors(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
class VendorBill(models.Model):
    STATUS_CHOICES = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
        ('Return', 'Return'),
        ('Claim', 'Claim'),
    ]
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vendor_bills/', blank=True, null=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    def __str__(self):
        return f"Vendor Bill {self.id} for {self.vendor.name}"


class MarketItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=100)
    qty = models.IntegerField()
    supplier = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.item}"
