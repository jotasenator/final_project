from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Issue, Profile

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


# register is no need it cause new users will be addressed by the admin, pass included


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


@login_required
def users(request):
    users = (
        User.objects.all()
        .exclude(is_superuser=True)
        .exclude(username="admin")
        .order_by("username")
    )
    return render(request, "capstone/users.html", {"users": users})


@login_required
def create_profile(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        address = request.POST["address"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        country_code = request.POST["country_code"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        picture = request.FILES.get("picture")

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "capstone/create_profile.html",
                {
                    "error": "A user with that username already exists",
                    "name": name,
                    "address": address,
                    "email": email,
                    "phone": phone,
                    "country_code": country_code,
                    "picture": picture,
                    "password": password,
                    "confirm_password": confirm_password,
                },
            )

        if password != confirm_password:
            return render(
                request,
                "capstone/create_profile.html",
                {
                    "error": "Passwords do not match",
                    "name": name,
                    "address": address,
                    "email": email,
                    "phone": phone,
                    "country_code": country_code,
                    "picture": picture,
                    "password": password,
                },
            )

        user = User.objects.create_user(username=username, password=password)

        profile = Profile(
            name = name,
            user = user,
            address = address,
            phone = phone,
            country_code = country_code,
            picture = picture,
            email = email,
        )
        profile.save()

        return render(
            request,
            "capstone/create_profile.html",
            {"message": "Profile created successfully"},
        )

    return render(request, "capstone/create_profile.html")


@login_required
def user_profile(request, username):
    profile = Profile.objects.get(user__username=username)
    return render(request, "capstone/user_profile.html", {"profile": profile})
