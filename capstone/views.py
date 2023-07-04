from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Issue

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from django.contrib import messages

from django.contrib.auth.decorators import login_required


def index(request, unknown_path=None):
    if unknown_path is not None:
        return redirect("index")
    return render(request, "capstone/index.html")


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "capstone/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure username is not empty
        if not username:
            return render(
                request,
                "capstone/register.html",
                {"message": "Username is required.", "username": username},
            )

        # Ensure email is not empty
        if not email:
            return render(
                request,
                "capstone/register.html",
                {"message": "Email is required.", "username": username, "email": email},
            )

        # Ensure password is not empty
        password = request.POST["password"]
        if not password:
            return render(
                request,
                "capstone/register.html",
                {
                    "message": "Password is required.",
                    "username": username,
                    "email": email,
                    "password": password,
                },
            )

        # Ensure confirmation is not empty
        confirmation = request.POST["confirmation"]
        if not confirmation:
            return render(
                request,
                "capstone/register.html",
                {
                    "message": "Confirmation is required.",
                    "username": username,
                    "email": email,
                    "password": password,
                },
            )

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request,
                "capstone/register.html",
                {
                    "message": "Passwords must match.",
                    "username": username,
                    "email": email,
                    "password": password,
                },
            )

        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            return render(
                request,
                "capstone/register.html",
                {
                    "message": e.messages[0],
                    "username": username,
                    "email": email,
                },
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "capstone/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")


@login_required
def submit_issue(request):
    print("submit_issue called")
    if request.method == "POST":
        user = request.user
        issue = request.POST["issue"]
        description = request.POST["description"]
        print(f"issue:{issue}")
        print(f"description:{description}")
        print(f"user:{user}")
        new_issue = Issue(issue=issue, description=description, user=user)
        new_issue.save()
        print(f"new_issue:{new_issue}")
        messages.success(request, "Your issue was submitted successfully!")
        return redirect("index")
    else:
        return render(request, "capstone/user.html")


@login_required
def reports(request):
    issues = Issue.objects.all().order_by("-created_at")
    print(f"reports {issues}")
    return render(request, "capstone/reports.html", {"issues": issues})

