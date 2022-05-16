from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        print(f"{email} {phone} {address}")
        contact = Contact(email=email, phone=phone, address=address)
        contact.save()
        return redirect('home')
    con = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': con})


def about(request):
    return render(request, 'about.html')


def dynamic_urls(request, slug):
    return render(request, 'dynamic.html', {'data': slug})


@login_required(login_url='/login/')
def todo_app(request):
    item_list = ToDo.objects.filter(user=request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            todo_form = TodoForm(request.POST)
            if todo_form.is_valid():
                # Return an object without saving to the DB
                obj = todo_form.save(commit=False)
                # Add an user field which will contain current user's id
                obj.user = User.objects.get(pk=request.user.id)
                obj.title = (request.POST.get('title')).capitalize()
                obj.content = (request.POST.get('content')).capitalize()
                obj.save()  # Save the final "real form" to the DB
                messages.info(request, f"Item Saved  with Title \"{(request.POST.get('title')).capitalize()}\" !!!")
                return redirect('todo-app')
        form = TodoForm()

        return render(request, 'todo.html', {
            "forms": form,
            "list": item_list,
            "title": "TODO LIST",
        })


def remove_todo(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo-app')


def mark_completed(request, item_id):
    item = ToDo.objects.get(id=item_id)
    if item.completed:
        messages.info(request, '"' + item.title + '"' +
        ' is already Marked as Completed')
    else:
        item.completed = True
        item.save()
        messages.info(request, '"' + item.title + '"' + ' Marked as Completed')
    return redirect('todo-app')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST.get('password')
        user_auth = authenticate(username=email, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect Username or Password ')
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Logout successfully.. !!!')
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        if password1 == password2:
            # print(f'{email} {password1} {password2}')
            user = User.objects.filter(username=email).first()
            if user:
                messages.info(request, 'User Already Exist')
                return redirect('login')
            user = User(email=email, username=email)
            user.set_password(password1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return redirect('login')
        else:
            messages.warning(request, 'Passwords are Different')
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')