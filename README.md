```markdown
# Blogverse — Django Blog Platform

A full-featured blog platform built with Django, supporting user authentication, rich blog creation, profile management, and image uploads.


![Home Page](https://github.com/user-attachments/assets/1f0cc4ee-894e-4ab1-b771-9fa04c3e9e49)
---

## Features

- Custom `AppUser` model with full authentication (signup, login, logout)
- Create, edit, delete, and search blog posts
- Like posts and manage your profile
- Image upload support via `Pillow`
- User profile pages with avatar and bio
- Responsive UI with Django templates
- Railway-ready deployment configuration

---

## Repository Structure

```
BLOGVERSE_DJANGO/
├── blogverse_project/
│   ├── Myblogproject/        # Django project config (settings, urls, wsgi)
│   ├── blogverse/            # Main app (models, views, templates, static)
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   ├── manage.py
│   └── requirements.txt
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.12+
- Django 5.1.7
- Pillow 11.1.0

---

## Setup and Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/taniyatandon/-blogverse-django.git
cd BLOGVERSE_DJANGO
```

### 2. Create and activate virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```powershell
cd blogverse_project
pip install -r requirements.txt
```

### 4. Apply migrations
```powershell
python manage.py migrate
```

### 5. Create a superuser (optional)
```powershell
python manage.py createsuperuser
```

### 6. Run the development server
```powershell
python manage.py runserver
```

Visit http://127.0.0.1:8000/

## Author

Made by [Taniya Tandon](https://github.com/taniyatandon)
```
