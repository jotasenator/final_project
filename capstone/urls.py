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
    path("users", views.users, name="users"),
    path("create_user", views.create_user, name="create_user"),
    path("user_profile/<str:username>", views.user_profile, name="user_profile"),
    path("customize_app", views.customize_app, name="customize_app"),
    path("create_pc", views.create_pc, name="create_pc"),
    path("pc_profile/<str:computer_name>", views.pc_profile, name="pc_profile"),
    path("pcs", views.pcs, name="pcs"),
    path("edit_pc/<str:computer_name>", views.edit_pc, name="edit_pc"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
