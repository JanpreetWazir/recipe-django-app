from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def home(request):
    return render(request, "home/index.html")

def contact(request):
    return render(request, "home/contact.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password_name')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('/signup/')  

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.set_password(password)  # Securely hash the password
        user.save()

        messages.success(request, "User created successfully!")
        return redirect('/login/')

    return render(request, "home/signup.html")

def login_path(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Wrong Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)  # Authenticate user

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('/')  # Redirect to home if login is successful
        else:
            messages.error(request, "Wrong Password")
            return redirect('/login/')

    return render(request, "home/login.html")


def logout_path(request):
    logout(request)
    return redirect('/login')