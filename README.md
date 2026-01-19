# Deployment Checklist

- Configure static files and install *whitenoise*
- Add environmental variables with *environs*
- create *.env* and update *.gitignore*
- update DEBUG, ALLOWED_HOSTS, SECRET_KEY, and CSRF_TRUSTED_ORIGINS
- update DATABASES to run PostgreSQL in production and install psycopg
- install *Gunicorn* as a production WSGI server
- create a *Procfile*
- update the requirements.txt file
- create a new Heroku project, push the code to it, and start a dyno web process.

## Static Files

For local usage, only two settings are required for static files:
  STATIC_URL, which is the base URLfor serving static files, and STATICFILES_DIRS, which defines the additional locations the built-in
staticfiles app will traverse looking for static files beyond an app/static folder.

 <!-- <-- django_project/settings.py -->
### local usage

- STATIC_URL = "static/"
- STATICFILES_DIRS = [BASE_DIR / "static"]

### production

The one configuration
required of us is setting STATIC_ROOT to define the location of compiled static files.

### Whitenoise

- Install whitenoise
- Add whitenoise to the INSTALLED_APPS above the built-in staticfiles app
- under MIDDLEWARE, add a new WhiteNoiseMiddleware on the third line
- change STORAGES to use WhiteNoise.

...
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
"default": {
"BACKEND": "django.core.files.storage.FileSystemStorage"
,
},
"staticfiles": {
"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
, # new
},
}

- run *collectstatic* command

## Environmental Variables (environs)

- Two are required (local and production)
- Install *environs*
- Import and Instantiate environs in *settings.py*
- Create new *.env* file in root dir and add to *.gitignore*

### .env

- Set DEBUG= False
- Set ALLOWED_HOSTS variables [localhost, 127.0.0.1, custom_domains]
- Run *python -c 'import
secrets; print(secrets.token_urlsafe())* on the command line.
- Set SECRET_KEY=value
- Set CORS_ALLOWED_HEADERS
- Set DATABASE_URL=value

### settings.py

- Set DEBUG = env.bool('DEBUG', default=False)
- Set SECRET_KEY = env.str('SECRET_KEY')
- Set CSRF_TRUSTED_ORIGIN
- install *psycopg* to connect app to database
- Set DATABASES = {"default": env.dj_db_url(DATABASE_URL)}

## Gunicorn and Procfile

- Install gunicorn
- Create Procfile
  - *web: gunicorn [django_project_name].wsgi*
- Update requirements.txt
