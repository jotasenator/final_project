from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("submit_issue", views.submit_issue, name="submit_issue"),
    path("reports", views.reports, name="reports"),
    path("issue/<int:issue_id>/delete/", views.delete_issue, name="delete_issue"),
    path("users", views.users, name="users"),
    path("create_user", views.create_user, name="create_user"),
    path("user_profile/<str:username>", views.user_profile, name="user_profile"),
    path("edit_user/<str:username>", views.edit_user, name="edit_user"),
    path("delete_user/<str:username>", views.delete_user, name="delete_user"),
    path("customize_app", views.customize_app, name="customize_app"),
    path("create_pc", views.create_pc, name="create_pc"),
    path("pc_profile/<str:computer_name>", views.pc_profile, name="pc_profile"),
    path("pcs", views.pcs, name="pcs"),
    path("edit_pc/<str:computer_name>", views.edit_pc, name="edit_pc"),
    path("delete_pc/<str:computer_name>", views.delete_pc, name="delete_pc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
