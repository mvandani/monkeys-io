DEBUG = True

ROOT_URL = "/"

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'monkeys',
            'USER': 'django',
            'PASSWORD': 'django',
            'HOST': 'localhost',
            'PORT': '5432',
            
        }
    }

SOCKETIO_HOST = '127.0.0.1'
SOCKETIO_PORT = 54890