from .models import SiteSettings

def global_settings(request):
    return {'site': SiteSettings.get()}
