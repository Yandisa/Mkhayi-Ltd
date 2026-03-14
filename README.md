# Mkhayi Ltd. — Django Website

A production-ready Django website for Mkhayi Ltd., fully managed through the admin panel.

---

## Quick Start

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Create your admin account
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver
```

Open **http://127.0.0.1:8000** to see the website.  
Open **http://127.0.0.1:8000/admin/** to manage all content.

---

## Admin Panel — What You Can Control

### Site Settings (one record, always there)
| Field | What it does |
|---|---|
| Company name / tagline | Appears in nav, footer, page title |
| Logo / Favicon | Upload PNG logo; browser tab icon |
| Phone / WhatsApp / Email / Address | Contact section + footer |
| Social media URLs | Facebook, Instagram, LinkedIn, Twitter |
| **Hero image** | Full-width banner photo (min 1600×900px) |
| Hero overlay darkness | 0.0 = fully visible photo, 1.0 = solid navy |
| Hero heading / subheading | Main headline and intro sentence |
| Hero CTA labels | Button text |
| **About image** | Team or office photo beside the About text |
| About heading / body | About section text |
| About stats | Years active, client count, installations |
| Services heading / subheading | Section header text |
| **Why Us image** | Photo shown beside the Why Us points |
| Why Us heading / body | Intro text for that section |
| **Contact image** | Photo shown under the contact details |
| Contact heading / subheading | CTA section text |
| Meta description / keywords | SEO tags |

### Services
Add as many as you like. Each card has:
- **Title** + **description**
- **Image** (upload a real photo — shown at the top of the card)
- **Icon** (shield, camera, wifi, lock, eye, wrench, etc.)
- **Highlight badge** (e.g. "24/7 Active", "HD Systems")
- **Order** — drag to reorder

### Gallery
Upload work photos organised by category (Security / CCTV / Fibre / General).  
The gallery section only appears on the site when at least one image is uploaded.

### Testimonials
Add client reviews. Each one has name, company, location, quote, rating (1–5 stars),  
and an optional client headshot. The section only appears when at least one is added.

### Why Us Points
Each point has a heading, body text, and icon name.  
Use: `check`, `star`, `shield`, `zap`, `users`, `clock`, `award`, `lock`

### Contact Messages
All form submissions land here. Mark as read once actioned.  
Superusers can delete old messages.

---

## Image Guidelines

| Section | Minimum size | Tips |
|---|---|---|
| Hero | 1600 × 900px | Landscape, dark subject matter works best |
| About | 800 × 1000px | Portrait orientation preferred |
| Why Us | 800 × 1000px | Portrait orientation preferred |
| Services | 600 × 400px | Landscape per service card |
| Gallery | 800 × 600px | Any ratio — grid adapts |
| Team / Testimonials | 400 × 400px | Square crop, headshot |
| Logo | 300 × 80px | Transparent PNG |

---

## Deploying to mkhayi.co.za

1. Set `DEBUG = False` in `settings.py`
2. Set `ALLOWED_HOSTS = ['mkhayi.co.za', 'www.mkhayi.co.za']`
3. Generate a strong `SECRET_KEY`
4. Run `python manage.py collectstatic`
5. Serve with **gunicorn** behind **nginx**
6. Point your domain's DNS to the server IP

---

## Project Structure

```
mkhayi_v2/
├── manage.py
├── requirements.txt
├── mkhayi_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/
    ├── models.py          ← SiteSettings, Service, Gallery, Testimonial…
    ├── admin.py           ← Full admin with image previews
    ├── views.py
    ├── urls.py
    ├── context_processors.py
    ├── templatetags/
    │   └── core_extras.py
    ├── migrations/
    │   └── 0001_initial.py
    ├── templates/core/
    │   └── home.html      ← Single-page site template
    └── static/core/
        ├── css/style.css  ← Full design system (white/gray/navy)
        └── js/main.js     ← Nav, scroll reveal, counters, back-to-top
```
