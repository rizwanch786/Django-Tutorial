from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_display = ['email_col', 'phone','less_address', 'view_record']
    readonly_fields = ('phone', 'email', 'address')
    search_fields = ('email', 'phone')
    def less_address(self, obj):
        return obj.address[:30]
    
    def email_col(self, obj):
        return format_html('<span style="color:red">' + obj.email + '...</span>')
    
    def view_record(self, obj):
        return format_html(f'<a href="/admin/tutorial/contact/{obj.id}" class="button button5">View</a>')