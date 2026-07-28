# CPS Legacy Chronicle

A comprehensive digital yearbook and academic portal built exclusively for Computer Science (CPS) students. The system enables students to register, create profiles, and generates a professional PDF yearbook — all managed through an intuitive admin dashboard.

## Features

### Authentication System
- User registration and login
- Password reset via email
- Show/hide password toggle (SVG eye icon)
- CPS matric validation (U21/CPS/XXXX, U22/CPS/XXXX, U23/CPS/XXXX only)

### Student System
- Student registration with image upload
- Full profile with bio, quote, skills, and preferences
- Admin approval workflow before public visibility
- Grid display (6 students per page) with search functionality
- Individual profile pages

### School Information Pages
- Vice Chancellor (VC) Page
- Faculty of Science Page
- Head of Department (HOD) Page
- Director of ICT Page
- Each with image, name, message, and description

### Lecturers Module
- Senior Lecturers (dynamic count)
- Junior Lecturers (dynamic count)
- Each with name, photo, title, and message

### Class Representative Page
- Class Rep profile with message to class
- Responsibilities listing

### Form Control System
- Admin sets form opening/closing dates
- Manual enable/disable registration
- Real-time status banner on homepage

### Admin Dashboard
- Modern UI with statistics cards
- Total students, approved, pending counts
- Lecturer count
- Approve/reject students
- Add/edit/delete lecturers
- Edit school pages (VC, Faculty, HOD, ICT)
- Control registration periods
- Manage site settings
- Generate yearbook PDF

### Digital Magazine System
- Auto-generated PDF yearbook
- Cover page with school branding
- School leadership pages
- Lecturer sections (Senior & Junior)
- Student profiles (3 per page)
- Print-ready format

### Design System
- Navy Blue (#0A1F44) + Gold (#D4AF37) theme
- Clean academic look
- Modern dashboard UI
- Card-based layouts
- Hover animations
- Fully responsive mobile design

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 6.0+ |
| Frontend | HTML, Tailwind CSS, JavaScript |
| Database | SQLite (development), PostgreSQL (production) |
| PDF | ReportLab |
| Image Processing | Pillow |

## Installation

### Prerequisites
- Python 3.10+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cps-legacy-chronicle.git
cd cps_legacy_chronicle
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (admin):
```bash
python manage.py createsuperuser
```

6. Initialize default data:
```bash
python manage.py shell -c "from school_pages.models import SchoolPage; SchoolPage.get_or_create_defaults()"
python manage.py shell -c "from core.models import FormControl; FormControl.get_instance()"
python manage.py shell -c "from core.models import SiteSettings; SiteSettings.get_instance()"
```

7. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the application.

## Project Structure

```
cps_legacy_chronicle/
├── cps_legacy/          # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI config
├── accounts/            # Authentication app
│   ├── models.py        # Custom User model
│   ├── views.py         # Login, register, password reset
│   ├── forms.py         # Authentication forms
│   └── urls.py          # Auth URL patterns
├── students/            # Student profiles app
│   ├── models.py        # Student model
│   ├── views.py         # Student list, detail, register
│   ├── forms.py         # Student forms
│   └── urls.py          # Student URL patterns
├── lecturers/           # Lecturers app
│   ├── models.py        # Lecturer model
│   ├── views.py         # Lecturer list
│   └── urls.py          # Lecturer URL patterns
├── school_pages/        # School info pages app
│   ├── models.py        # SchoolPage model
│   ├── views.py         # VC, Faculty, HOD, ICT pages
│   └── urls.py          # School pages URL patterns
├── yearbook/            # PDF generation app
│   ├── views.py         # Yearbook PDF generation
│   └── urls.py          # Yearbook URL patterns
├── admin_portal/        # Admin dashboard app
│   ├── views.py         # Admin management views
│   ├── forms.py         # Admin forms
│   └── urls.py          # Admin URL patterns
├── core/                # Core functionality
│   ├── models.py        # FormControl, SiteSettings
│   ├── views.py         # Home, about, contact
│   ├── context_processors.py  # Global template context
│   └── middleware.py    # Custom middleware
├── templates/           # All HTML templates
├── static/              # CSS, JS, images
├── media/               # User-uploaded files
└── requirements.txt     # Python dependencies
```

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Deployment

### Using Render (Free)
1. Create a `render.yaml` file
2. Connect your GitHub repository to Render
3. Deploy as a Web Service

### Using PythonAnywhere
1. Upload files via Git
2. Set up virtual environment
3. Configure WSGI
4. Collect static files

### Production Settings
- Set `DEBUG=False`
- Use PostgreSQL database
- Configure `ALLOWED_HOSTS`
- Set up email backend for password reset
- Run `python manage.py collectstatic`

## Matric Validation Rules

Only the following matric formats are accepted:
- U21/CPS/XXXX (e.g., U21/CPS/1234)
- U22/CPS/XXXX (e.g., U22/CPS/1234)
- U23/CPS/XXXX (e.g., U23/CPS/1234)

## Admin Access

1. Create a superuser: `python manage.py createsuperuser`
2. Access admin at: `/admin/`
3. Or use the admin dashboard at: `/admin-portal/`

## Core Workflow

1. Student registers with CPS-validated matric number
2. Admin approves student in dashboard
3. Student logs in and creates profile
4. Student accesses their dashboard
5. All approved students and lecturers are displayed publicly
6. Admin generates PDF yearbook
7. Yearbook is available for download

## License

This project is built for academic purposes for the Computer Science Department.

## Credits

Built for the CPS Class of 2026.
