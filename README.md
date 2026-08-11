# KleenChamps Africa — Django Website

## Quick Start

### 1. Install dependencies
```bash
pip install django pillow
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. Create admin user
```bash
python manage.py createsuperuser
```

### 4. Run the server
```bash
python manage.py runserver
```

Open http://127.0.0.1:8000 for the website  
Open http://127.0.0.1:8000/admin/ for the admin panel

## Admin Login (pre-created)
- **Username:** `admin`
- **Password:** `kleenchamps2024`
  
> ⚠️ Change this password immediately in production!

## Admin Features
- View all client inquiries with color-coded service badges
- Filter by service type, read/unread status, date
- Search by name, email, company, or message content
- Mark inquiries as read/unread in bulk
- Add internal notes to any inquiry
- Full Django admin interface branded to KleenChamps Africa

## Updating Before/After Images
Replace the images in `core/static/images/` with your actual project photos.  
The website uses: `project_page-22.jpg`, `project_page-23.jpg`, `project_page-24.jpg`, `project_page-25.jpg`

After replacing images, run:
```bash
python manage.py collectstatic
```

## Production Deployment
1. Set `DEBUG = False` in `kleenchamps/settings.py`
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` with your domain
4. Use gunicorn + nginx for serving
5. Configure a real database (PostgreSQL recommended)
