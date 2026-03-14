from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import AdminSite

admin.site.site_header = 'Mkhayi Ltd. Administration'
admin.site.site_title = 'Mkhayi Ltd.'
admin.site.index_title = 'Site Management Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
