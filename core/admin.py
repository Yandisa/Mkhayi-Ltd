from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import (
    SiteSettings, Service, TeamMember,
    Testimonial, GalleryImage, WhyUsPoint, ContactMessage
)


def img_preview(url, height=60):
    if url:
        return format_html('<img src="{}" style="height:{}px;border-radius:4px;object-fit:cover;" />', url, height)
    return '—'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🏢  Brand & Identity', {
            'fields': ('company_name', 'tagline', 'logo', 'favicon'),
            'description': 'Upload a transparent PNG logo for best results.'
        }),
        ('📞  Contact Details', {
            'fields': ('phone', 'whatsapp_number', 'email', 'address'),
        }),
        ('🔗  Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url', 'twitter_url'),
            'classes': ('collapse',),
        }),
        ('🖼️  Hero Section', {
            'fields': (
                'hero_image', 'hero_image_overlay',
                'hero_heading', 'hero_subheading',
                'hero_cta_label', 'hero_cta_secondary',
            ),
            'description': 'Upload a full-width image (min 1600×900px). Adjust overlay darkness to keep text legible.'
        }),
        ('ℹ️  About Section', {
            'fields': (
                'about_heading', 'about_body',
                'about_image', 'about_image_caption',
                'about_years', 'about_clients', 'about_projects',
            ),
        }),
        ('🛠️  Services Section Header', {
            'fields': ('services_heading', 'services_subheading'),
            'description': 'Manage individual service cards in the Services section below.'
        }),
        ('✅  Why Choose Us', {
            'fields': ('why_heading', 'why_body', 'why_image'),
            'description': 'Manage individual bullet points in the "Why Us Points" section.'
        }),
        ('📬  Contact / CTA Section', {
            'fields': ('contact_heading', 'contact_subheading', 'contact_image'),
        }),
        ('🔍  SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('logo_preview', 'hero_preview', 'about_preview', 'why_preview', 'contact_preview')

    def logo_preview(self, obj):
        return img_preview(obj.logo.url if obj.logo else None, 50)
    logo_preview.short_description = 'Logo Preview'

    def hero_preview(self, obj):
        return img_preview(obj.hero_image.url if obj.hero_image else None, 80)
    hero_preview.short_description = 'Hero Preview'

    def about_preview(self, obj):
        return img_preview(obj.about_image.url if obj.about_image else None, 80)
    about_preview.short_description = 'About Preview'

    def why_preview(self, obj):
        return img_preview(obj.why_image.url if obj.why_image else None, 80)
    why_preview.short_description = 'Why Us Preview'

    def contact_preview(self, obj):
        return img_preview(obj.contact_image.url if obj.contact_image else None, 80)
    contact_preview.short_description = 'Contact Preview'

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Auto-redirect to the single instance
        obj, _ = SiteSettings.objects.get_or_create(pk=1)
        from django.shortcuts import redirect
        return redirect(f'/admin/core/sitesettings/{obj.pk}/change/')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display  = ('order', 'image_thumb', 'title', 'icon', 'highlight', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'icon', 'order', 'is_active')
        }),
        ('Content', {
            'fields': ('description', 'highlight', 'image'),
            'description': 'Upload a service image (min 600×400px). The highlight is shown as a badge on the card.'
        }),
    )

    def image_thumb(self, obj):
        return img_preview(obj.image.url if obj.image else None, 40)
    image_thumb.short_description = 'Image'


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display  = ('order', 'photo_thumb', 'name', 'role', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('name',)

    def photo_thumb(self, obj):
        return img_preview(obj.photo.url if obj.photo else None, 40)
    photo_thumb.short_description = 'Photo'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display  = ('photo_thumb', 'client_name', 'company', 'location', 'rating', 'is_active')
    list_editable = ('is_active',)
    list_display_links = ('client_name',)

    def photo_thumb(self, obj):
        return img_preview(obj.photo.url if obj.photo else None, 40)
    photo_thumb.short_description = 'Photo'


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ('order', 'image_thumb', 'caption', 'category', 'is_active')
    list_editable = ('order', 'category', 'is_active')
    list_display_links = ('caption',)
    list_filter   = ('category', 'is_active')

    def image_thumb(self, obj):
        return img_preview(obj.image.url if obj.image else None, 50)
    image_thumb.short_description = 'Image'


@admin.register(WhyUsPoint)
class WhyUsPointAdmin(admin.ModelAdmin):
    list_display  = ('order', 'icon', 'heading', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('heading',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ('submitted_at', 'name', 'email', 'phone', 'service', 'is_read')
    list_filter     = ('is_read', 'service')
    list_editable   = ('is_read',)
    search_fields   = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'service', 'message', 'submitted_at')
    ordering        = ('-submitted_at',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
