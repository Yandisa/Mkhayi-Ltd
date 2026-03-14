from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

admin.site.site_header = 'Mkhayi Ltd. Administration'
admin.site.site_title = 'Mkhayi Ltd.'
admin.site.index_title = 'Site Management Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # Always serve media files regardless of DEBUG
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
