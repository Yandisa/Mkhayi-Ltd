from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteSettings, Service, TeamMember, Testimonial, GalleryImage, WhyUsPoint, ContactMessage


def home(request):
    site        = SiteSettings.get()
    services    = Service.objects.filter(is_active=True)
    team        = TeamMember.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    gallery     = GalleryImage.objects.filter(is_active=True)
    why_points  = WhyUsPoint.objects.filter(is_active=True)

    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        phone   = request.POST.get('phone', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email,
                phone=phone, service=service,
                message=message,
            )
            messages.success(request, 'Thank you! We will be in touch with you shortly.')
            return redirect('home')
        else:
            messages.error(request, 'Please complete all required fields.')

    return render(request, 'core/home.html', {
        'site':         site,
        'services':     services,
        'team':         team,
        'testimonials': testimonials,
        'gallery':      gallery,
        'why_points':   why_points,
    })
