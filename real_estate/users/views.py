from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "users/login.html")


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "The username is already taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "The email is already taken")
                    return redirect("register")
                else:
                    user = User.objects.create_user(  # type: ignore
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    auth.login(request, user)
                    messages.success(request, "You are now logged in")
                    return redirect("index")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")
    else:
        return render(request, "users/register.html")


def logout(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect("index")
    else:
        return HttpResponse("<h1>405 Not allowed</h1>")
