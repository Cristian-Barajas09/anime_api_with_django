"""Configuracion para distintas bases de datos"""
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'anime_api',
        'USER': 'postgres',
        'PASSWORD': '300804',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
