from django.db import models
from django.utils import timezone
import psycopg2

class Customer(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Token(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=150)

    def __str__(self):
        return f"Token for {self.customer.name} on {self.date}"

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('Checking', 'Checking'),
        ('Pending', 'Pending'),
        ('Repairing', 'Repairing'),
        ('Return', 'Return'),
        ('Received', 'Received'),
        ('OK', 'OK'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    item = models.CharField(max_length=100)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    advance = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


    def __str__(self):
        return f"Invoice {self.id} for {self.customer.name}"