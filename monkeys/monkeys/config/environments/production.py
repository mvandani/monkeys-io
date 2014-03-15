DEBUG = False
INCLUDE_RSVP = False

ROOT_URL = "/"

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'monkeys',
            'USER': 'monkeys',
            'PASSWORD': 'monkeys',
            'HOST': 'monkeys.io',
            'PORT': '5432',
        }
    }