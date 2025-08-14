

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent  
# used to represent the root folder of django project

SECRET_KEY = 'django-insecure-*u7jge#pmpd14wqb717^kg32**t18fti9+c9e4#5ip(eu3w2)a'  
# it is generated automatically.it is unique for each app and also.
# it is used for cryptographic signing like session cookies also csrf token.
# if the key is leaked we can change that also  (using django key generator)


DEBUG = True
# it is used to show detaild error msg
# it show:
# The line where the error occurred
# The values of local variables
# Suggestions to fix the issue
# 🟢 It's very helpful for developers during coding and testing.


# if it is true in production it is very dangerous bcz attackers can see folder structure ,varable in memory ,installed apps.
# if it is false in  developemnt 
# no detailed error showing
# static files not loaded



ALLOWED_HOSTS = []

# if the debug is false then django check this list if the domain include this list only navigate to that domain
# other domain show 400 bad request


INSTALLED_APPS = [
    'django.contrib.admin',  Enables the admin dashboard to manage models.
    'django.contrib.auth',  Adds authentication features : login, logout, users, passwords, permissions.
    'django.contrib.contenttypes',used to track all models
    'django.contrib.sessions',Enables Session Managment
    'django.contrib.messages', Manage temporary msgs (like "Login successful")
    'django.contrib.staticfiles', Enable static files during dev  in production it use cloud services like aws vercel like that
    'Form' 
]

# it show all django used apps it contain build in and also we can add our apps also

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',adding security features .http to https redirecting 
    'django.contrib.sessions.middleware.SessionMiddleware',enable session support .track user via session cookies
    'django.middleware.common.CommonMiddleware',add helping features like add slash to urls
    'django.middleware.csrf.CsrfViewMiddleware',protect site from csrf attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',used to check authentication
    'django.contrib.messages.middleware.MessageMiddleware',enable msg framework it show success/info/arror msg in template 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',prevent from clickjacking.embeded to another site
]
# middleware is like a bridge between the request and response in Django.
# ▶️ Request
# This is the HTTP request that comes from the user's browser to your Django web server.
# ▶️ Response
# This is the HTTP response that Django sends back to the user's browser.



ROOT_URLCONF = 'project.urls'
# tell the django to look the root url 


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',DjangoTemplates it is used to render templates
        'DIRS': [],here we declare location of project level template
        'APP_DIRS': True,true aanel check direct app inside templates folder automatic call aakum 
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'
# used to deploy app on wsgi compatibale web server


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Here we use sqlite3 as default db.we can change that using change engine to postgresql my sql


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',it check similarity of user name email passsword.if it similar blocked
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',it check min length satisfied or not
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',it block common passwords qwerty,123456789 like that
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',not support full number password 
    },
]
# it is used to check password details.like strong 


LANGUAGE_CODE = 'en-us'
# represned english us  
TIME_ZONE = 'UTC'
USE_I18N = True
# it means djando support every language.also support translation
# multi language support
USE_TZ = True
# data store in server utc timezone 


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
# here we represent staic files


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# django generate some field for tables like if 
