"""
Authentication routes
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def log_in(request):
    """
    Log the user in
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            pass

    return render(request, "auth/login.html")


def log_out(request):
    """
    Log the user out
    """

    logout(request)

    return redirect("home")


def register(request):
    """
    Register a new user
    """

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(request, "Registration successful.")

            return redirect("home")

        messages.error(request, "Registration failed.")

    form = UserCreationForm()

    return render(request, "auth/register.html", {"form": form})
