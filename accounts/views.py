from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from .forms import RegisterForm, LoginForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Registration Successful."
            )

            return redirect("dashboard")

    else:

        form = RegisterForm()

    return render(
        request,
        "pages/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                "Login Successful."
            )

            return redirect("dashboard")

    else:

        form = LoginForm()

    return render(
        request,
        "pages/login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged Out Successfully."
    )

    return redirect("index")