from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        print(f"{email} {phone} {address}")
        contact = Contact(email = email, phone = phone, address = address)
        contact.save()
        return redirect('home')
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def dynamic_urls(request, slug):
    return render(request, 'dynamic.html', {'data':slug})
