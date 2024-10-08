from django.urls import path, reverse_lazy
import os

ALLOWED_HOSTS = ['localhost']

MAX_IMAGE_SIZE = 3 * 1024 * 1024  #10 Mb

STATICFILES_DIRS = [
    "E:\\toni\\sigte\\projectes\\rutes_saludables2\\static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'rutes_saludables2',
        'USER': 'postgres',
        'PASSWORD': 'p1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
} 

GDAL_LIBRARY_PATH = 'C:/OSGeo4W/bin/gdal303.dll'
GEOS_LIBRARY_PATH = 'C:/OSGeo4W/bin/geos_c.dll'