from django.contrib import admin
from .models import User, Issue, Profile, Footer, Intranet


# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Footer)
admin.site.register(Intranet)


class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(Issue, IssueAdmin)
