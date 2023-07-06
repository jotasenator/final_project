from .models import Footer


def footer_processor(request):
    footer = Footer.objects.first()
    return {
        "company_name": footer.company_name,
        "company_address": footer.company_address,
        "company_phone": footer.company_phone,
        "company_email": footer.company_email,
        "company_avatar": footer.company_avatar,
    }
