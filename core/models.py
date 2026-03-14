from django.db import models
from django.core.exceptions import ValidationError


class SiteSettings(models.Model):
    """Singleton — controls every text, image and contact detail on the site."""

    # ── Brand
    company_name        = models.CharField(max_length=200, default='Mkhayi Ltd.')
    tagline             = models.CharField(max_length=300, default='Your Trusted Security & Technology Partner')
    logo                = models.ImageField(upload_to='brand/', blank=True, null=True,
                                            help_text='Transparent PNG recommended, min 300px wide')
    favicon             = models.ImageField(upload_to='brand/', blank=True, null=True,
                                            help_text='32×32 or 64×64 .ico / .png')

    # ── Contact
    phone               = models.CharField(max_length=30, default='+27 74 415 3970')
    whatsapp_number     = models.CharField(max_length=30, default='27744153970',
                                           help_text='Digits only, no + or spaces. E.g. 27744153970')
    email               = models.EmailField(default='info@mkhayi.co.za')
    address             = models.TextField(default='South Africa', blank=True)

    # ── Social
    facebook_url        = models.URLField(blank=True)
    instagram_url       = models.URLField(blank=True)
    linkedin_url        = models.URLField(blank=True)
    twitter_url         = models.URLField(blank=True)

    # ── Hero Section
    hero_heading        = models.CharField(max_length=120, default='Protecting What Matters Most',
                                           help_text='Short punchy headline')
    hero_subheading     = models.TextField(default='Professional security services, CCTV supply & installation, and fibre connectivity across South Africa.',
                                           help_text='One or two sentences shown below the headline')
    hero_cta_label      = models.CharField(max_length=60, default='Get a Free Quote')
    hero_cta_secondary  = models.CharField(max_length=60, default='Our Services')
    hero_image          = models.ImageField(upload_to='hero/', blank=True, null=True,
                                            help_text='Full-width banner — min 1600×900px JPG/PNG')
    hero_image_overlay  = models.DecimalField(max_digits=3, decimal_places=2, default=0.55,
                                              help_text='Overlay darkness 0.0 (none) to 1.0 (full black)')

    # ── About Section
    about_heading       = models.CharField(max_length=120, default='Built on Trust & Expertise')
    about_body          = models.TextField(default=(
        'Mkhayi Ltd. is a proudly South African company delivering integrated security and technology '
        'solutions. From armed response and CCTV systems to high-speed fibre installations, we cover '
        'everything your home or business needs to stay protected and connected. We combine industry '
        'expertise with honest, transparent service — so you always know exactly what you are getting.'
    ))
    about_image         = models.ImageField(upload_to='about/', blank=True, null=True,
                                            help_text='Team or operations photo — min 800×600px')
    about_image_caption = models.CharField(max_length=200, blank=True,
                                           default='Our team in the field')
    about_years         = models.PositiveIntegerField(default=5,  help_text='Years in operation')
    about_clients       = models.PositiveIntegerField(default=500, help_text='Happy clients served')
    about_projects      = models.PositiveIntegerField(default=800, help_text='Installations completed')

    # ── Services Section
    services_heading    = models.CharField(max_length=120, default='What We Do')
    services_subheading = models.TextField(default='Comprehensive security and technology solutions tailored for residential and commercial clients across South Africa.',
                                           blank=True)

    # ── Why Us Section
    why_heading         = models.CharField(max_length=120, default='Why Choose Mkhayi?')
    why_body            = models.TextField(default=(
        "We don't just sell products — we build lasting partnerships. "
        "Every installation is backed by our experienced team, transparent pricing, and a commitment "
        "to after-sales support that keeps your systems running long after the first handshake."
    ))
    why_image           = models.ImageField(upload_to='why/', blank=True, null=True,
                                            help_text='Operatives or equipment photo — min 800×600px')

    # ── Contact / CTA Section
    contact_heading     = models.CharField(max_length=120, default="Let's Secure Your Future")
    contact_subheading  = models.TextField(default='Reach out for a no-obligation quote. We respond within one business day.',
                                           blank=True)
    contact_image       = models.ImageField(upload_to='contact/', blank=True, null=True,
                                            help_text='Background image for the contact strip')

    # ── SEO
    meta_description    = models.TextField(blank=True,
                                           default='Mkhayi Ltd. — security services, CCTV installation, and fibre connectivity across South Africa.')
    meta_keywords       = models.CharField(max_length=300, blank=True,
                                           default='security services, CCTV, fibre installation, South Africa, Mkhayi')

    class Meta:
        verbose_name        = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # prevent deletion

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Service(models.Model):
    ICON_CHOICES = [
        ('shield',   'Shield — Security'),
        ('camera',   'Camera — CCTV'),
        ('wifi',     'Wifi — Fibre / Network'),
        ('lock',     'Lock — Access Control'),
        ('eye',      'Eye — Monitoring'),
        ('wrench',   'Wrench — Maintenance'),
        ('zap',      'Zap — Electrical'),
        ('globe',    'Globe — Connectivity'),
        ('users',    'Users — Guarding'),
        ('activity', 'Activity — Response'),
    ]

    title       = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True, blank=True)
    description = models.TextField(help_text='Two or three sentences describing this service')
    image       = models.ImageField(upload_to='services/', blank=True, null=True,
                                    help_text='Service illustration — min 600×400px')
    icon        = models.CharField(max_length=20, choices=ICON_CHOICES, default='shield')
    highlight   = models.CharField(max_length=80, blank=True,
                                   help_text='Short bold stat or selling point, e.g. "24/7 Active"')
    order       = models.PositiveSmallIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering    = ['order', 'title']
        verbose_name = 'Service'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class TeamMember(models.Model):
    name        = models.CharField(max_length=100)
    role        = models.CharField(max_length=100)
    bio         = models.TextField(blank=True)
    photo       = models.ImageField(upload_to='team/', blank=True, null=True,
                                    help_text='Headshot — min 400×400px, square crop')
    order       = models.PositiveSmallIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} — {self.role}'


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company     = models.CharField(max_length=100, blank=True)
    location    = models.CharField(max_length=100, blank=True, default='South Africa')
    quote       = models.TextField()
    photo       = models.ImageField(upload_to='testimonials/', blank=True, null=True,
                                    help_text='Client headshot — optional, 200×200px')
    rating      = models.PositiveSmallIntegerField(default=5,
                                                   choices=[(i, f'{i} stars') for i in range(1, 6)])
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.client_name} — {self.company or self.location}'


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('security', 'Security Services'),
        ('cctv',     'CCTV Installations'),
        ('fibre',    'Fibre Installations'),
        ('general',  'General'),
    ]
    image    = models.ImageField(upload_to='gallery/', help_text='Min 800×600px')
    caption  = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    order    = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.caption or f'Image {self.pk}'


class WhyUsPoint(models.Model):
    heading     = models.CharField(max_length=80)
    body        = models.TextField()
    icon        = models.CharField(max_length=20, default='check',
                                   help_text='Icon name: check, star, shield, zap, users, clock, award, lock')
    order       = models.PositiveSmallIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Why Us Point'

    def __str__(self):
        return self.heading


class ContactMessage(models.Model):
    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    phone        = models.CharField(max_length=30, blank=True)
    service      = models.CharField(max_length=100, blank=True)
    message      = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read      = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Message'

    def __str__(self):
        return f'{self.name} — {self.email} ({self.submitted_at.strftime("%d %b %Y")})'
