# type: ignore
# flake8: noqa

# GERADOR SECRET_KEYS
""" import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
"""

SECRET_KEY = 'CHANGE-ME'

DEBUG = False

# Seu domínio ou IP devem vir aqui
ALLOWED_HOSTS = [
    'SEU_DOMINIO_OU_IP',
]  # Troque * para seu domínio ou IP

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'CHANGE-ME',
        'USER': 'CHANGE-ME',
        'PASSWORD': 'CHANGE-ME',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
