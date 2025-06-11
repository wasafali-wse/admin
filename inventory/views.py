from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Customer, Invoice, Token




def home(request):
    return render(request, 'home.html')
def customer_invoice_detail(request, customer_id, invoice_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    invoice = get_object_or_404(Invoice, pk=invoice_id, customer=customer)
    # You can pass any data to template
    context = {
        'customer': customer,
        'invoice': invoice,
    }
    return render(request, 'invoice_detail.html', context)

def customer_token_detail(request, customer_id, token_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    token = get_object_or_404(Token, pk=token_id, customer=customer)
    context = {
        'customer': customer,
        'token': token,
    }
    return render(request, 'token_detail.html', context)

def customer_overview(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    invoices = Invoice.objects.filter(customer=customer)
    tokens = Token.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'invoices': invoices,
        'tokens': tokens,
    }
    return render(request, 'customer.html', context)