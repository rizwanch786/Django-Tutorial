from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import * 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
    con = Contact.objects.all()
    return render(request, 'contact.html', {'contacts':con})

def about(request):
    return render(request, 'about.html')

def dynamic_urls(request, slug):
    return render(request, 'dynamic.html', {'data':slug})

def todo_app(request):
    item_list = ToDo.objects.order_by("-published_date")
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            messages.info(request, "item Saved !!!")
            return redirect('todo-app')
    form = TodoForm()
    
    return render(request, 'todo.html', {
             "forms" : form,
             "list" : item_list,
             "title" : "TODO LIST",
           })

def remove_todo(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo-app')

def mark_completed(request, item_id):
    item = ToDo.objects.get(id = item_id)
    item.completed = True
    item.save()
    return redirect('todo-app')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST.get('password')
        # print(f'{email} {password}')
        user_auth = authenticate(request, username=email, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    
    
def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            # print(f'{email} {password1} {password2}')
            user = User.objects.filter(username = email).first()
            if user:
                messages.info(request, 'User Already Exist')
                return redirect('login')
            user = User(email = email, username = email)
            user.set_password(password1)
            user.save()
            return redirect('login')
        else:
            messages.warning(request, 'Passwords are Different')
    return render(request, 'signup.html')