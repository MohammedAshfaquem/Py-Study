# ✅ INSTALLED_APPS
# Purpose:
# Lists all Django apps (built-in and custom) that are enabled for your project.
# INSTALLED_APPS = [
#     'django.contrib.admin',     # Admin interface
#     'django.contrib.auth',      # Authentication system
#     'django.contrib.contenttypes', 
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'myapp',                    # Your custom app
# ]
# 🔸 Apps listed here are registered with Django and can provide models, templates, static files, etc.

# ✅ MIDDLEWARE
# Purpose:
# A list of middleware classes that process requests/responses globally.
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
# ]
# 🔸 Middleware can handle sessions, security, authentication, etc., before/after the view logic runs.

# ✅ DATABASES
# Purpose:
# Defines database configurations. By default, Django uses SQLite.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',  # Or 'postgresql', 'mysql', etc.
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }
# 🔸 You can switch to PostgreSQL, MySQL, etc., by changing the ENGINE and related settings.

# ✅ TEMPLATES
# Purpose:
# Tells Django where to look for HTML templates and how to render them.
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],  # Custom templates folder
#         'APP_DIRS': True,  # Look in each app’s templates folder
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
# 🔸 The context processors inject variables into all templates (like request, user, etc.)

# ✅ STATICFILES_DIRS
# Purpose:
# Tells Django where to find additional static files in development.
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
# 🔸 This is only needed for development. In production, use collectstatic.

# ✅ AUTHENTICATION_BACKENDS
# Purpose:
# Specifies how Django will authenticate users.
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',  # Default
# ]
# 🔸 You can add custom or third-party backends here (e.g., for social login, LDAP, etc.)