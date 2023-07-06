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
    path("create_profile", views.create_profile, name="create_profile"),
    path("user_profile/<str:username>", views.user_profile, name="user_profile"),
    path("customize_app", views.customize_app, name="customize_app"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
