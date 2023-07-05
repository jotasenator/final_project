from django.contrib import admin
from .models import User, Issue, Profile


# Register your models here.
admin.site.register(User)
admin.site.register(Profile)


class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(Issue, IssueAdmin)
