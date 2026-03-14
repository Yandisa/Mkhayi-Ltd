"""
Seed migration — populates SiteSettings, Services, WhyUsPoints,
and links the bundled placeholder images so the site is ready
immediately after `python manage.py migrate`.
"""
from django.db import migrations


def seed(apps, schema_editor):
    SiteSettings = apps.get_model('core', 'SiteSettings')
    Service      = apps.get_model('core', 'Service')
    WhyUsPoint   = apps.get_model('core', 'WhyUsPoint')
    GalleryImage = apps.get_model('core', 'GalleryImage')

    # ── SiteSettings ────────────────────────────────────────
    site, _ = SiteSettings.objects.get_or_create(pk=1)
    site.company_name        = 'Mkhayi Ltd.'
    site.tagline             = 'Your Trusted Security & Technology Partner'
    site.phone               = '+27 74 415 3970'
    site.whatsapp_number     = '27744153970'
    site.email               = 'info@mkhayi.co.za'
    site.address             = 'South Africa'
    site.hero_heading        = 'Protecting What\nMatters Most'
    site.hero_subheading     = (
        'Professional security services, CCTV supply & installation, '
        'and high-speed fibre connectivity across South Africa.'
    )
    site.hero_cta_label      = 'Get a Free Quote'
    site.hero_cta_secondary  = 'Our Services'
    site.hero_image          = 'hero/hero_main.jpg'
    site.hero_image_overlay  = '0.62'
    site.about_heading       = 'Built on Trust & Expertise'
    site.about_body          = (
        'Mkhayi Ltd. is a proudly South African company delivering integrated security '
        'and technology solutions. From professional guarding and CCTV systems to '
        'high-speed fibre installations, we cover everything your home or business '
        'needs to stay protected and connected. We combine industry expertise with '
        'honest, transparent service — so you always know exactly what you are getting.'
    )
    site.about_image         = 'about/about_main.jpg'
    site.about_image_caption = 'Our team, always on duty'
    site.about_years         = 5
    site.about_clients       = 500
    site.about_projects      = 800
    site.services_heading    = 'What We Do'
    site.services_subheading = (
        'Comprehensive security and technology solutions tailored for '
        'residential estates, commercial properties, and businesses across South Africa.'
    )
    site.why_heading         = 'Why Choose Mkhayi?'
    site.why_body            = (
        "We don't just sell products — we build lasting partnerships. "
        "Every installation is backed by our experienced team, transparent pricing, "
        "and after-sales support that keeps your systems running long after the first handshake."
    )
    site.why_image           = 'why/why_us.jpg'
    site.contact_heading     = "Let's Secure Your Future"
    site.contact_subheading  = (
        'Reach out for a no-obligation quote. We respond within one business day.'
    )
    site.contact_image       = 'contact/contact_bg.jpg'
    site.meta_description    = (
        'Mkhayi Ltd. — professional security services, CCTV supply & installation, '
        'and fibre connectivity across South Africa.'
    )
    site.save()

    # ── Services ────────────────────────────────────────────
    services_data = [
        {
            'title': 'Security Services',
            'slug': 'security-services',
            'description': (
                'Professional manned guarding for residential estates, commercial '
                'properties, and events. All guards are PSIRA-registered, thoroughly '
                'vetted, and trained to the highest industry standards.'
            ),
            'icon': 'shield',
            'highlight': 'PSIRA Registered',
            'image': 'services/security_services.jpg',
            'order': 1,
        },
        {
            'title': 'CCTV Supply & Installation',
            'slug': 'cctv-installation',
            'description': (
                'We supply and install high-definition CCTV camera systems for homes '
                'and businesses. Full coverage includes remote viewing, night vision, '
                'motion detection, and cloud or local recording options.'
            ),
            'icon': 'camera',
            'highlight': 'HD Systems',
            'image': 'services/cctv_installation.jpg',
            'order': 2,
        },
        {
            'title': 'Fibre Installation',
            'slug': 'fibre-installation',
            'description': (
                'End-to-end fibre optic installation for homes and commercial premises. '
                'We handle the full process from site survey and cabling right through '
                'to activation, testing, and ongoing support.'
            ),
            'icon': 'wifi',
            'highlight': 'Fast Speeds',
            'image': 'services/fibre_installation.jpg',
            'order': 3,
        },
        {
            'title': 'Access Control',
            'slug': 'access-control',
            'description': (
                'Smart access control solutions including biometric readers, electric '
                'gates, intercom systems, and keypad entry — keeping unauthorised '
                'persons out while giving approved users seamless access.'
            ),
            'icon': 'lock',
            'highlight': '24/7 Active',
            'image': '',
            'order': 4,
        },
        {
            'title': '24/7 Monitoring',
            'slug': 'monitoring',
            'description': (
                'Round-the-clock remote monitoring of your CCTV and alarm systems. '
                'Our control room operators respond immediately to any alert, '
                'dispatching response teams within minutes of an incident.'
            ),
            'icon': 'eye',
            'highlight': 'Always Watching',
            'image': '',
            'order': 5,
        },
        {
            'title': 'Maintenance & Support',
            'slug': 'maintenance',
            'description': (
                'Regular system health checks, camera cleaning, software updates, '
                'and emergency call-outs ensure your equipment performs reliably '
                'every day. Service level agreements available.'
            ),
            'icon': 'wrench',
            'highlight': 'Fast Response',
            'image': '',
            'order': 6,
        },
    ]

    for data in services_data:
        img = data.pop('image')
        svc, _ = Service.objects.get_or_create(slug=data['slug'], defaults=data)
        if img:
            svc.image = img
        for k, v in data.items():
            setattr(svc, k, v)
        svc.save()

    # ── Why Us Points ────────────────────────────────────────
    why_data = [
        ('PSIRA Registered & Compliant',
         'Fully licenced and compliant with all South African Private Security Industry Regulatory Authority requirements.',
         'award', 1),
        ('Rapid Deployment',
         'Fast on-site response and quick installation turnaround — because security cannot wait.',
         'zap', 2),
        ('Transparent Pricing',
         'Clear, upfront quotes with zero hidden fees. Monthly website hosting from just R150, full package R180.',
         'check', 3),
        ('Dedicated After-Sales Support',
         'Our relationship does not end at installation. We provide ongoing support, monitoring, and emergency call-outs.',
         'users', 4),
    ]

    for heading, body, icon, order in why_data:
        WhyUsPoint.objects.get_or_create(
            heading=heading,
            defaults={'body': body, 'icon': icon, 'order': order}
        )

    # ── Gallery ──────────────────────────────────────────────
    GalleryImage.objects.get_or_create(
        image='gallery/cctv_install_01.jpg',
        defaults={
            'caption': 'CCTV installation at commercial premises',
            'category': 'cctv',
            'order': 1,
        }
    )


def unseed(apps, schema_editor):
    pass  # non-destructive reverse


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(seed, unseed),
    ]
