import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static/media'

# Load the appropriate .env file based on ENVIRONMENT
env_name = os.getenv("ENVIRONMENT", "development").lower()
env_path = BASE_DIR / f".env.{env_name}"
# load_dotenv(dotenv_path=env_path if env_path.exists() else BASE_DIR / ".env")
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print(f"✅ Loaded environment: {env_path.name}")
else:
    print(f"✅ Loaded environment: {env_path.name}")
    raise FileNotFoundError(f"❌ Cannot find environment file: {env_path}")
# Load t

# General environment setup
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()
DEBUG = os.getenv("DEBUG", "False") == "True"

# Domains
DOMAINS = {
    "development": os.getenv("DEVELOPMENT_DOMAIN"),
    "staging": os.getenv("STAGING_DOMAIN"),
    "production": os.getenv("PROD_DOMAIN"),
}

# Raise a helpful error if a domain is missing for the active env
DOMAIN = DOMAINS.get(ENVIRONMENT)
if not DOMAIN:
    raise Exception(f"{ENVIRONMENT.upper()}_DOMAIN is not set in the environment.")

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# ALLOWED_HOSTS = (os.getenv("ALLOWED_HOSTS") or DOMAIN or "localhost").split(",")
ALLOWED_HOSTS = [
    h.strip() for h in (os.getenv("ALLOWED_HOSTS") or DOMAIN or "localhost").split(",")
]

AUTH_USER_MODEL = "accounts.User"

# Security
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("SECRET_KEY is not set in the environment!")

# Email
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "webmaster@localhost")
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND",
    (
        "django.core.mail.backends.console.EmailBackend"
        if DEBUG
        else "django.core.mail.backends.smtp.EmailBackend"
    ),
)
EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 25))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "False") == "True"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "False") == "True"

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "rest_framework",
    "rest_framework_simplejwt",
    "allauth",
    "allauth.account",
    "corsheaders",
    # Local
    "accounts",
    "portfolio",
    "analytics",
    "api",
    "dashboard",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # High priority
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "smart_portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "smart_portfolio.wsgi.application"

# Database
# Environment-aware prefix
DB_PREFIX = ENVIRONMENT.upper()  # e.g., DEVELOPMENT, STAGING, PRODUCTION

DATABASES = {
    "default": {
        "ENGINE": os.getenv(f"{DB_PREFIX}_DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv(f"{DB_PREFIX}_DB_NAME"),
        "USER": os.getenv(f"{DB_PREFIX}_DB_USER"),
        "PASSWORD": os.getenv(f"{DB_PREFIX}_DB_PASSWORD"),
        "HOST": os.getenv(f"{DB_PREFIX}_DB_HOST", "localhost"),
        "PORT": os.getenv(f"{DB_PREFIX}_DB_PORT", "5432"),
    }
}
required_db_keys = ["NAME", "USER", "PASSWORD"]
for key in required_db_keys:
    if not DATABASES["default"].get(key):
        raise Exception(f"❌ Missing required DB setting: {DB_PREFIX}_DB_{key}")

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("accounts.middleware.JWTAuthWith2FA",),
}

# CORS policy
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Only allow all in development
