# Blogverse Django Project

A full-featured Django blog application with custom user authentication, blog creation, editing, search, profiles, and image uploads.

## Features

- Custom `AppUser` model for authentication
- User signup, login, logout, and profile management
- Write, edit, and delete blog posts
- Search posts and like posts
- Image upload support with `Pillow`
- Static templates and responsive UI powered by Django templates
- Ready for local development and deployment

## Repository Structure

- `blogverse_project/`
  - `Myblogproject/` — Django project configuration
  - `blogverse/` — main Django app containing models, views, templates, and static files
  - `requirements.txt` — required Python packages for this app
- `.gitignore` — ignores virtual environments, database file, media, and editor artifacts

## Requirements

Install using the provided requirements file:

```powershell
cd blogverse_project
pip install -r requirements.txt
```

Current dependencies:

- `Django==5.1.7`
- `Pillow==11.1.0`

## Setup and Run Locally

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
cd blogverse_project
pip install -r requirements.txt
```

3. Apply database migrations:

```powershell
python manage.py migrate
```

4. Create a superuser (optional):

```powershell
python manage.py createsuperuser
```

5. Start the development server:

```powershell
python manage.py runserver
```

6. Open the app in your browser at `http://127.0.0.1:8000/`

## Notes

- Do not commit the `.venv/`, `db.sqlite3`, or `media/` directories.
- The project uses SQLite for local development.
- Keep `DEBUG = True` only for local development and disable it before production.

## Deployment

This project is already configured with `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for deployment to Railway. For production, use environment variables for `SECRET_KEY` and set `DEBUG = False`.
