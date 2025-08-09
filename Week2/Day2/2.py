# Static Files in Django
# Definition:
# Static files are assets like CSS, JavaScript, and images used to style and enhance the front-end of a Django application.

# 1. Configuration in settings.py:
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]  # For development
# STATIC_URL: URL prefix for referencing static files (e.g., /static/css/style.css)
 
# STATICFILES_DIRS: Tells Django where to look for your custom static files during development (optional but commonly used)

# 2. Loading Static Files in Templates:
# In your HTML templates:
# {% load static %}
# <link rel="stylesheet" href="{% static 'css/style.css' %}">
# {% load static %}: Loads the static template tag.

# {% static 'path/to/file' %}: Resolves to the full static file URL.

# 3. Folder Structure Example:
# project/
# ├── static/
# │   ├── css/
# │   │   └── style.css
# │   └── js/
# │       └── script.js
# ├── app/
# │   └── templates/
# │       └── index.html
# 4. Collecting Static Files for Production:
# For deployment:
# python manage.py collectstatic
# This command gathers all static files into STATIC_ROOT for efficient serving by a production server (like Nginx).