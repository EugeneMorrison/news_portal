from allauth.socialaccount.models import SocialApp
from django.contrib.sites.shortcuts import get_current_site

def configured_social_providers(request):
    site = get_current_site(request)
    apps = SocialApp.objects.filter(sites=site)
    providers = [app.provider for app in apps]
    return {
        'configured_providers': providers
    }