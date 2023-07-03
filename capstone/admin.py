from django.contrib import admin
from .models import User, Issue


# Register your models here.
admin.site.register(User)


class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(Issue, IssueAdmin)
