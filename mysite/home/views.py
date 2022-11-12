from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
# Create your views here.


def index(request):
    context = {
        "variable1": "this is sent",
        "variable2": "welcome to the jungle"
    }
    # messages.success(request, "this is a test message")
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, surname=surname, email=email,
                          phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')

    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")


def login(request):
    if request.method == "POST":
        # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(user)
            # A backend authenticated the credentials
            return redirect("/blog")
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials
        # check if user has entered correct credentials

    return render(request, 'login.html')


def blog(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'blog.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')
