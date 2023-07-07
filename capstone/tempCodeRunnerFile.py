urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("submit_issue", views.submit_issue, name="submit_issue"),
    path("reports", views.reports, name="reports"),
    path("users", views.users, name="users"),
    path("create_user", views.create_user, name="create_user"),
    path("user_profile/<str:username>", views.user_profile, name="user_profile"),

    path("<path:unknown_path>", views.index),  # unknown_path should remain last !!!
]