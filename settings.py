# ...existing code...
INSTALLED_APPS = [
    # ...existing code...
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'students',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  
    # ...existing code...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Optionally, configure CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # Add other origins as needed
]
# ...existing code...
