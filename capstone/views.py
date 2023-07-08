from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import User, Issue, Profile, Footer, Intranet, Computer

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import ComputerForm


def index(request, unknown_path=None):
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


def delete_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.delete()
    return redirect("reports")


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
def create_user(request):
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
                "capstone/create_user.html",
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
                "capstone/create_user.html",
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
            name=name,
            user=user,
            address=address,
            phone=phone,
            country_code=country_code,
            picture=picture,
            email=email,
        )
        profile.save()

        return render(
            request,
            "capstone/create_user.html",
            {"message": "User created successfully"},
        )

    return render(request, "capstone/create_user.html")


@login_required
def user_profile(request, username):
    profile = Profile.objects.get(user__username=username)
    return render(request, "capstone/user_profile.html", {"profile": profile})


@login_required
def delete_user(request, username):
    user = get_object_or_404(User, username=username)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect("users")


@login_required
def customize_app(request):
    footer = Footer.objects.first()
    intranet = Intranet.objects.first()

    if request.method == "POST":
        footer.company_name = request.POST["company_name"]
        footer.company_address = request.POST["company_address"]
        footer.company_phone = request.POST["company_phone"]
        footer.company_email = request.POST["company_email"]
        # even if is conditional it access to company_avatar so we need to check if it's not empty
        if "company_avatar" in request.FILES:
            footer.company_avatar = request.FILES["company_avatar"]
        footer.save()

        intranet.company_intranet = request.POST["company_intranet"]

    return render(request, "capstone/customize_app.html")


@login_required
def create_pc(request):
    users = (
        User.objects.all()
        .exclude(is_superuser=True)
        .exclude(username="admin")
        .order_by("username")
    )

    if request.method == "POST":
        department = request.POST["department"]
        responsible = request.POST["responsible"]

        form = ComputerForm(request.POST)
        if form.is_valid():
            computer = form.save(
                commit=False
            )  # commit=False is to not save the computer to the database yet
            computer.department = department
            computer.responsible = responsible
            computer.save()
            messages.success(request, "Computer created successfully!")
            return redirect("create_pc")
    else:
        form = ComputerForm()

    return render(
        request,
        "capstone/create_pc.html",
        {
            "users": users,
            "form": form,
        },
    )


@login_required
def pcs(request):
    pcs = Computer.objects.all().order_by("-department", "computer_name")
    return render(request, "capstone/pcs.html", {"pcs": pcs})


@login_required
def pc_profile(request, computer_name):
    computer = get_object_or_404(Computer, computer_name=computer_name)
    return render(request, "capstone/pc_profile.html", {"computer": computer})


@login_required
def edit_pc(request, computer_name):
    computer = get_object_or_404(Computer, computer_name=computer_name)

    users = (
        User.objects.all()
        .exclude(is_superuser=True)
        .exclude(username="admin")
        .order_by("username")
    )

    if request.method == "POST":
        department = request.POST["department"]
        responsible = request.POST["responsible"]

        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            computer = form.save(
                commit=False
            )  # commit=False is to not save the computer to the database yet
            computer.department = department
            computer.responsible = responsible
            computer.save()
            messages.success(request, "Computer updated successfully!")
            return redirect("edit_pc", computer_name=computer_name)
    else:
        form = ComputerForm(instance=computer)

    return render(request, "capstone/edit_pc.html", {"form": form, "users": users})


@login_required
def delete_pc(request, computer_name):
    computer = get_object_or_404(Computer, computer_name=computer_name)
    computer.delete()
    messages.success(request, "Computer deleted successfully!")
    return redirect("pcs")
