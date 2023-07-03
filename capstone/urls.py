from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("submit_issue", views.submit_issue, name="submit_issue"),
    path("<path:unknown_path>", views.index),  # unknown_path should remain last !!!
]
