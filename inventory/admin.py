from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from django.shortcuts import get_object_or_404, render
from .models import Customer, Token, Invoice

# --- Print view functions ---
def print_token_view(request, token_id):
    token = get_object_or_404(Token, pk=token_id)
    return render(request, 'admin/print_token.html', {'token': token})

def print_invoice_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    return render(request, 'admin/print_invoice.html', {'invoice': invoice})

# --- Inline for Token ---
class TokenInline(admin.TabularInline):
    model = Token
    extra = 0
    readonly_fields = ('print_button',)
    fields = ('description', 'date', 'print_button')

    def print_button(self, obj):
        if obj and obj.pk:
            url = reverse('admin:token-print', args=[obj.pk])
            return format_html('<a class="button" href="{}" target="_blank">Print Token</a>', url)
        return ''
    print_button.short_description = 'Print'

# --- Inline for Invoice ---
class InvoiceInline(admin.TabularInline):
    model = Invoice
    extra = 0
    readonly_fields = ('print_button',)
    fields = ('item', 'qty', 'gross_amount', 'advance', 'discount', 'balance', 'status', 'print_button')

    def print_button(self, obj):
        if obj and obj.pk:
            url = reverse('admin:invoice-print', args=[obj.pk])
            return format_html('<a class="button" href="{}" target="_blank">Print Invoice</a>', url)
        return ''
    print_button.short_description = 'Print'

# --- Register Customer with inlines ---
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_filter = ('date', 'name', 'contact')
    search_fields = ('name', 'contact')
    list_display = ('id', 'date', 'name', 'contact')
    inlines = [TokenInline, InvoiceInline]

    def get_urls(self):
        # Register URLs for print views
        urls = super().get_urls()
        custom_urls = [
            path('admin/token/<int:token_id>/print/', self.admin_site.admin_view(print_token_view), name='token-print'),
            path('admin/invoice/<int:invoice_id>/print/', self.admin_site.admin_view(print_invoice_view), name='invoice-print'),
        ]
        return custom_urls + urls